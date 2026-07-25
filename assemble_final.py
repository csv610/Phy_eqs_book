#!/usr/bin/env python3
"""Assemble individual chapter files into the final physics_equations_final.tex."""
import os, re

CHAPTERS_DIR = "chapters"
OUTPUT = "physics_equations_final.tex"

chapter_files = sorted([f for f in os.listdir(CHAPTERS_DIR) if f.endswith('.tex')])

with open("physics_equations_restructured.tex") as f:
    content = f.read()

preamble_match = re.search(r'(.*?)(?=\\chapter\{)', content, re.DOTALL)
preamble = preamble_match.group(1) if preamble_match else ""

chapter_contents = []
for fname in chapter_files:
    with open(os.path.join(CHAPTERS_DIR, fname)) as f:
        chapter_contents.append(f.read().strip())

with open(OUTPUT, 'w') as f:
    f.write(preamble + "\n\n")
    for i, ch_content in enumerate(chapter_contents):
        f.write(ch_content + "\n\n")
        if i < len(chapter_contents) - 1:
            f.write("%=============================================================\n\n")

print(f"Assembled {len(chapter_contents)} chapters into {OUTPUT}")
with open(OUTPUT) as f:
    lines = f.readlines()
print(f"Total lines: {len(lines)}")
