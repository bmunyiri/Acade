from pathlib import Path

from fileops import line

path  = Path("crosswd.txt")
contents = path.read_text()

lines = [contents.splitlines()]

for line in lines:
    line += lines
print(line[:20])
print(len(lines))