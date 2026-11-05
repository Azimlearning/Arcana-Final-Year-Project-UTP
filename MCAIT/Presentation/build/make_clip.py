"""Cuts assets/arcana-demo.mp4 from the screen recording and real-model screenshots (brag-style, silent).

Usage: python make_clip.py <frames_dir> <marks.json>
The presenter speaks over it, so there is no soundtrack.
"""
import json
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

FRAMES, MARKS = Path(sys.argv[1]), json.load(open(sys.argv[2]))
HERE = Path(__file__).resolve().parent
ASSETS = HERE / "assets"
WORK = FRAMES.parent / "clip"
WORK.mkdir(exist_ok=True)
EVIDENCE = Path(r"C:\Users\User\Documents\FYP DOCS\Arcana-v2\refdocs\evidence")
W, H, FPS = 1920, 1080, 30
NAVY, GOLD = (7, 30, 68), (219, 172, 72)
IX, IY, IW, IH = 176, 14, 1568, 882
BOLD = r"C:\Windows\Fonts\calibrib.ttf"
REG = r"C:\Windows\Fonts\calibri.ttf"


def run(args):
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error"] + [str(a) for a in args], check=True)


def caption(name, kicker, line):
    """A full-frame navy plate with a window for the footage and the caption beneath it."""
    im = Image.new("RGBA", (W, H), NAVY + (255,))
    d = ImageDraw.Draw(im)
    d.rectangle((IX, IY, IX + IW - 1, IY + IH - 1), fill=(0, 0, 0, 0))
    d.text((IX, IY + IH + 16), kicker.upper(), font=ImageFont.truetype(BOLD, 28), fill=GOLD)
    d.text((IX, IY + IH + 50), line, font=ImageFont.truetype(BOLD, 44), fill="white")
    p = WORK / f"cap-{name}.png"
    im.save(p)
    return p


def card(name, title, sub):
    im = Image.new("RGB", (W, H), NAVY)
    d = ImageDraw.Draw(im)
    d.text((140, 390), title, font=ImageFont.truetype(BOLD, 92), fill="white")
    d.text((144, 520), sub, font=ImageFont.truetype(REG, 50), fill=GOLD)
    p = WORK / f"card-{name}.png"
    im.save(p)
    return p


def still(name, src, secs, kicker, line, crop=None):
    """A real screenshot with a slow push-in and a caption."""
    im = Image.open(src).convert("RGB")
    sw, sh = im.size
    k = sw / 1440
    im = im.crop(crop and tuple(int(c * k) for c in crop) or (0, 0, sw, int(810 * k)))
    plate = Image.open(caption(name, kicker, line)).convert("RGBA")
    n = int(secs * FPS)
    out = WORK / f"seg-{name}.mp4"
    enc = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                            "-vf", f"fade=in:st=0:d=0.25,fade=out:st={secs - 0.25}:d=0.25,format=yuv420p",
                            "-c:v", "libx264", "-crf", "21", "-preset", "medium", str(out)], stdin=subprocess.PIPE)
    iw, ih = im.size
    for i in range(n):
        z = 1 + 0.05 * i / n  # slow push-in
        cw, ch = iw / z, ih / z
        x0, y0 = (iw - cw) / 2, (ih - ch) / 2
        fr = im.resize((IW, IH), Image.BICUBIC, box=(x0, y0, x0 + cw, y0 + ch))
        canvas = Image.new("RGBA", (W, H), "white")
        canvas.paste(fr, (IX, IY))
        canvas.alpha_composite(plate)
        enc.stdin.write(canvas.convert("RGB").tobytes())
    enc.stdin.close()
    enc.wait()
    return out


def card_seg(name, title, sub, secs):
    out = WORK / f"seg-{name}.mp4"
    run(["-loop", "1", "-i", card(name, title, sub), "-vf",
         f"fade=in:st=0:d=0.3,fade=out:st={secs - 0.3}:d=0.3,format=yuv420p", "-t", secs, "-r", FPS,
         "-c:v", "libx264", "-crf", "20", "-preset", "medium", out])
    return out


def rec_seg(name, start, end, speed, kicker, line):
    dur = (end - start) / speed
    out = WORK / f"seg-{name}.mp4"
    run(["-ss", start, "-to", end, "-i", WORK / "recording.mp4", "-i", caption(name, kicker, line), "-filter_complex",
         f"[0:v]setpts=(PTS-STARTPTS)/{speed},scale={IW}:{IH}[v];color=white:s={W}x{H}:r={FPS}[bg];[bg][v]overlay={IX}:{IY}:shortest=1[b];[b][1:v]overlay=0:0,fade=in:st=0:d=0.2,"
         f"fade=out:st={dur - 0.25:.3f}:d=0.25,format=yuv420p", "-r", FPS, "-c:v", "libx264", "-crf", "21", "-preset", "medium", out])
    return out


# Constant-frame-rate master from the screencast.
run(["-f", "concat", "-safe", "0", "-i", FRAMES / "list.txt", "-vf", f"scale={W}:{H}:force_original_aspect_ratio=decrease,pad={W}:{H}:(ow-iw)/2:(oh-ih)/2:white,format=yuv420p",
     "-r", FPS, "-c:v", "libx264", "-crf", "16", "-preset", "fast", WORK / "recording.mp4"])

m = MARKS
segs = [
    card_seg("open", "Arcana: the paper in practice", "16 retrieval papers. The interface follows the question.", 2.6),
    still("q1", EVIDENCE / "p2-d1-17-live-q-cross-10-graph-and-path.png", 4.2, "A relational question, real model",
          "A cited summary, and a graph where each edge cites its sentence"),
    still("q2", EVIDENCE / "p2-d1-14-live-comparison-grid-after-fix.png", 4.2, "A comparison, real model",
          'A grid: each cell quotes its source, or says "No evidence in this paper"'),
    still("q3", EVIDENCE / "p2-d1-15-live-control-q-single-01.png", 3.4, "A question the corpus cannot answer, real model",
          "It says so, instead of inventing an answer"),
    rec_seg("notes", m["graph"] - 1.5, m["concept"] + 0.4, 1.7, "Learning tools, no model call",
            "Concept pages built from the extracted graph"),
    rec_seg("links", m["concept"] + 0.4, m["concept-links"] + 0.1, 1.0, "Grounded links",
            "Every stated relation shows the sentence and page behind it"),
    rec_seg("quiz", m["quiz"] - 2.0, m["quiz-answered"] + 0.1, 1.3, "Quiz from the learner's own documents",
            "A wrong answer is corrected, and the graph recolours by mastery"),
    rec_seg("lab", m["lab"] - 3.2, m["lab-moved"] + 0.2, 1.25, "Verified lab, test function",
            "Offered only where a stored passage states the formula"),
]
lst = WORK / "segs.txt"
lst.write_text("".join(f"file '{s.as_posix()}'\n" for s in segs))
out = ASSETS / "arcana-demo.mp4"
run(["-f", "concat", "-safe", "0", "-i", lst, "-c:v", "libx264", "-crf", "23", "-preset", "slow", "-pix_fmt", "yuv420p",
     "-movflags", "+faststart", "-an", out])
print("clip", out, round(out.stat().st_size / 1e6, 1), "MB")
