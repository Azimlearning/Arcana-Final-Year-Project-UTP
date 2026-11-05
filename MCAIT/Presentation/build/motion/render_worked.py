"""Renders the real-data videos, and cuts the shorter clips from the existing films.

python render_worked.py stills
python render_worked.py video
"""
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from playwright.sync_api import sync_playwright

HERE = Path(__file__).resolve().parent
ASSETS = HERE.parent / "assets"
FPS = 30
VIDS = {"ingest": [5.6, 15.4], "traverse": [8.8, 16.4], "fuse": [6.2, 14.4], "adaptive": [2.5, 6.0, 9.5, 13.0]}
mode = sys.argv[1]
if len(sys.argv) > 2:
    VIDS = {sys.argv[2]: VIDS[sys.argv[2]]}


def cut(src, start, end, out):
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", str(start), "-to", str(end), "-i", str(ASSETS / src),
                    "-c:v", "libx264", "-crf", "21", "-preset", "slow", "-pix_fmt", "yuv420p", "-movflags", "+faststart", "-an", str(ASSETS / out)], check=True)


with sync_playwright() as p:
    b = p.chromium.launch(channel="msedge")
    pg = b.new_page(viewport={"width": 1920, "height": 1080})
    for v, stills in VIDS.items():
        pg.goto(HERE.joinpath("worked.html").as_uri() + f"?v={v}")
        pg.evaluate("document.fonts.ready")
        if mode == "stills":
            for i, t in enumerate(stills):
                pg.evaluate(f"render({t})")
                pg.screenshot(path=str(ASSETS / f"worked-{v}-{i}.png"))
        else:
            dur = pg.evaluate("DURATION")
            tmp = Path(tempfile.mkdtemp(prefix=v))
            for i in range(int(dur * FPS)):
                pg.evaluate(f"render({i / FPS})")
                pg.screenshot(path=str(tmp / f"f{i:05d}.jpg"), type="jpeg", quality=92)
            subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(FPS), "-i", str(tmp / "f%05d.jpg"), "-c:v", "libx264", "-crf", "20",
                            "-preset", "slow", "-pix_fmt", "yuv420p", "-movflags", "+faststart", "-an", str(ASSETS / f"video-{v}.mp4")], check=True)
            shutil.rmtree(tmp)
            print(v, round((ASSETS / f"video-{v}.mp4").stat().st_size / 1e6, 2), "MB")
    b.close()
if mode != "stills" and len(sys.argv) == 2:
    cut("arcana-explainer.mp4", 14.8, 22.0, "video-compose.mp4")
    cut("arcana-explainer.mp4", 22.0, 29.0, "video-bound.mp4")
    cut("arcana-demo.mp4", 2.6, 14.4, "video-demo-questions.mp4")
    cut("arcana-demo.mp4", 14.4, 35.93, "video-demo-tools.mp4")
    print("cuts done")
