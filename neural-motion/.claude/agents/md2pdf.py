#!/usr/bin/env python3
"""Render an SOP markdown file to PDF using the repo's sop_pdf_style.css + headless Chrome."""
import html
import pathlib
import subprocess
import sys
import tempfile

import mistune

ROOT = pathlib.Path("/home/neotix/Documents/SOPs/neural-motion")
CSS = (ROOT / ".claude/agents/sop_pdf_style.css").read_text()

src = pathlib.Path(sys.argv[1]).resolve()
out = pathlib.Path(sys.argv[2]).resolve()

md = mistune.create_markdown(plugins=["table", "strikethrough"])
body = md(src.read_text())
title = html.escape(src.stem.replace("_", " "))
page = (
    f"<!doctype html>\n<html><head><meta charset='utf-8'>"
    f"<title>{title}</title><style>\n{CSS}\n</style></head>\n<body>\n{body}\n</body></html>\n"
)

with tempfile.TemporaryDirectory() as tmp:
    tmp_html = pathlib.Path(tmp) / f"{src.stem}.html"
    tmp_html.write_text(page)
    subprocess.run(
        [
            "google-chrome",
            "--headless=new",
            "--disable-gpu",
            "--no-sandbox",
            "--no-pdf-header-footer",
            f"--print-to-pdf={out}",
            tmp_html.as_uri(),
        ],
        check=True,
        capture_output=True,
    )
print(f"wrote {out} ({out.stat().st_size} bytes)")
