from pathlib import Path
import json

guests = ["John", "Peter", "Mary"]
lines = "\n".join(json.dumps(g) for g in guests)
Path("guest.txt").write_text(lines)