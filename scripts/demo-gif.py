#!/usr/bin/env python3
"""Render the animated demo GIF for the README hero (docs/screenshots/demo.gif).

Like `scripts/screenshots.sh`, this drives the **real release `crozier` binary**
against the committed demo spec (`screenshots/petstore.yml`) — so the summary
line and the generated file it reveals are genuine CLI output, captured live (no
mocks). crozier is a single-shot command with no live view to screen-record, so
the "animation" is an honest reconstruction of a terminal SESSION: a user typing
`crozier generate …`, the real summary appearing, then `cat`-ing one of the files
crozier just wrote and watching it stream in. Frames are drawn with the same
**vendored, pinned JetBrains Mono font** (`screenshots/fonts/`) the SVG
screenshots use, so the result is deterministic and self-contained (Pillow only —
no ttyd/ffmpeg).

The GIF is informational, like the screenshots — it is NOT hash-gated (a GIF is
not byte-reproducible across Pillow versions), so it is regenerated on demand
with `just screenshots-gif` and committed to `docs/screenshots/demo.gif`.
"""

from __future__ import annotations

import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

# GitHub-dark palette, matching the SVG screenshots' window (bg #0d1117).
BG = (13, 17, 23)
BAR = (22, 27, 34)
FG = (201, 209, 217)
DIM = (139, 148, 158)
GREEN = (63, 185, 80)
RED = (248, 81, 73)
YELLOW = (210, 153, 34)
CYAN = (57, 197, 207)
PURPLE = (188, 140, 255)
DOTS = [(255, 95, 86), (255, 189, 46), (39, 201, 63)]  # traffic-light window dots

FONT_SIZE = 20
PAD = 24
BAR_H = 40
TYPE_STEP = 3       # characters revealed per typing frame
TYPE_MS = 45        # per typing frame
LINE_MS = 70        # per revealed output line
BEAT_MS = 500       # pause after a command's output
HOLD_MS = 3200      # hold on the final frame

PY_KEYWORDS = {
    "import", "from", "class", "def", "if", "return", "self", "enum", "str",
    "typing",
}


def run_summary(binp: str, spec: str, work: str) -> str:
    """The genuine one-line summary crozier prints (relative --output, so the
    path in the message is the bare `sdk`, stable on every machine)."""
    env = dict(os.environ)
    proc = subprocess.run(
        [binp, "generate", "--spec", spec, "--output", "sdk",
         "--package-name", "petstore", "--project-name", "petstore"],
        cwd=work, env=env, capture_output=True, text=True,
    )
    return (proc.stderr or proc.stdout).strip().splitlines()[-1]


def colorize(text: str) -> list[tuple[str, tuple[int, int, int]]]:
    """Light token coloring for a generated Python line — enough to read as code,
    no full lexer. A comment dims the whole line; otherwise keywords, strings, and
    the enum values get a color and the rest stays foreground."""
    if text.lstrip().startswith("#"):
        return [(text, DIM)]
    segs: list[tuple[str, tuple[int, int, int]]] = []
    for tok in re.split(r'(\s+|[(),:\[\]=."]|\b)', text):
        if not tok:
            continue
        if tok.startswith('"') or tok.endswith('"'):
            color = YELLOW
        elif tok in PY_KEYWORDS:
            color = PURPLE
        elif tok.isupper() and tok.isalpha():
            color = CYAN            # enum members (AVAILABLE, PENDING, SOLD)
        else:
            color = FG
        segs.append((tok, color))
    return segs


# A frame is a list of lines; a line is a list of (text, color) segments.
def prompt_line(shown: str, done: bool) -> list:
    """A `$` prompt with `shown` chars of the command typed so far, plus a block
    cursor while still typing."""
    line = [("$ ", GREEN), (shown, FG)]
    if not done:
        line.append(("█", DIM))   # block cursor
    return line


def type_frames(frames: list, base: list, command: str) -> None:
    """Append frames that type `command` after the prompt, char-stepped."""
    for i in range(0, len(command) + 1, TYPE_STEP):
        frames.append((base + [prompt_line(command[:i], False)], TYPE_MS))
    frames.append((base + [prompt_line(command, True)], TYPE_MS))


def build_frames(binp: str, spec: str, work: str, model: list[str]) -> list:
    summary = run_summary(binp, spec, work)
    gen_cmd = "crozier generate --spec petstore.yml --output sdk"
    cat_cmd = "cat sdk/src/petstore/types/pet_status.py"

    frames: list = []
    base: list = []

    # 1. Type the generate command, then reveal the summary.
    type_frames(frames, base, gen_cmd)
    base = base + [prompt_line(gen_cmd, True)]
    base = base + [[(summary, FG)]]
    frames.append((base, BEAT_MS))
    base = base + [[("", FG)]]        # spacer line

    # 2. Type the cat command, then stream the generated file in line by line.
    type_frames(frames, base, cat_cmd)
    base = base + [prompt_line(cat_cmd, True)]
    for line in model:
        base = base + [colorize(line)]
        frames.append((base, LINE_MS))

    frames.append((base, HOLD_MS))    # hold on the finished session
    return frames


def render_gif(frames: list, font_path: str, out: str) -> None:
    font = ImageFont.truetype(font_path, FONT_SIZE)
    cw = int(font.getlength("M"))
    asc, desc = font.getmetrics()
    lh = asc + desc + 6
    rows = max(len(f[0]) for f in frames)
    cols = max((sum(len(t) for t, _ in line) for f in frames for line in f[0]), default=1)
    width = PAD * 2 + max(cols, 52) * cw
    height = BAR_H + PAD + rows * lh + PAD

    def draw_frame(lines: list) -> Image.Image:
        img = Image.new("RGB", (width, height), BG)
        d = ImageDraw.Draw(img)
        d.rectangle([0, 0, width, BAR_H], fill=BAR)
        for i, col in enumerate(DOTS):
            cx = PAD + i * 22
            cy = BAR_H // 2
            d.ellipse([cx - 6, cy - 6, cx + 6, cy + 6], fill=col)
        y = BAR_H + PAD
        for segs in lines:
            x = PAD
            for text, color in segs:
                d.text((x, y), text, font=font, fill=color)
                x += int(font.getlength(text))
            y += lh
        return img

    imgs = [draw_frame(lines) for lines, _ in frames]
    durations = [ms for _, ms in frames]
    imgs[0].save(
        out, save_all=True, append_images=imgs[1:], duration=durations,
        loop=0, optimize=True, disposal=2,
    )


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    binp = os.environ.get("CROZIER_BIN", str(root / "target/release/crozier"))
    spec = str(root / "screenshots/petstore.yml")
    font_path = str(root / "screenshots/fonts/JetBrainsMono-Regular.ttf")
    out = os.environ.get("DEMO_GIF_OUT", str(root / "docs/screenshots/demo.gif"))

    for p in (binp, spec, font_path):
        if not Path(p).exists():
            print(f"demo-gif: missing {p}", file=sys.stderr)
            return 1

    with tempfile.TemporaryDirectory(prefix="crozier-gif-") as work:
        summary_ok = run_summary(binp, spec, work)
        model_path = Path(work) / "sdk/src/petstore/types/pet_status.py"
        if not model_path.exists() or not summary_ok:
            print("demo-gif: crozier did not produce the expected output", file=sys.stderr)
            return 1
        model = model_path.read_text().rstrip("\n").splitlines()
        frames = build_frames(binp, spec, work, model)

    Path(out).parent.mkdir(parents=True, exist_ok=True)
    render_gif(frames, font_path, out)
    print(f"demo-gif: wrote {out} ({len(frames)} frames)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
