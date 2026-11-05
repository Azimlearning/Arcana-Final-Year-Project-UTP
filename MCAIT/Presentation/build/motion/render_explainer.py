"""Renders explainer.html frame by frame (each frame is a pure function of time).

python render_explainer.py stills          -> settled stills in assets/
python render_explainer.py video           -> assets/arcana-explainer.mp4
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
STILLS = {"visual-problem": 4.1, "visual-graph": 9.5, "visual-fusion": 14.3, "visual-compose": 21.4, "visual-bound": 28.5}
CHECK = {"mid-gate": 19.1, "mid-trans": 10.0}

mode = sys.argv[1]
with sync_playwright() as p:
    b = p.chromium.launch(channel="msedge")
    pg = b.new_page(viewport={"width": 1920, "height": 1080})
    pg.goto(HERE.joinpath("explainer.html").as_uri())
    pg.evaluate("document.fonts.ready")
    if mode == "stills":
        for name, t in {**STILLS, **CHECK}.items():
            pg.evaluate(f"render({t})")
            pg.screenshot(path=str(ASSETS / f"{name}.png"))
        print("stills done")
    else:
        dur = pg.evaluate("DURATION")
        tmp = Path(tempfile.mkdtemp(prefix="explainer"))
        n = int(dur * FPS)
        for i in range(n):
            pg.evaluate(f"render({i / FPS})")
            pg.screenshot(path=str(tmp / f"f{i:05d}.jpg"), type="jpeg", quality=92)
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(FPS), "-i", str(tmp / "f%05d.jpg"),
                        "-c:v", "libx264", "-crf", "20", "-preset", "slow", "-pix_fmt", "yuv420p", "-movflags", "+faststart", "-an",
                        str(ASSETS / "arcana-explainer.mp4")], check=True)
        shutil.rmtree(tmp)
        print("video", (ASSETS / "arcana-explainer.mp4").stat().st_size / 1e6, "MB")
    b.close()
