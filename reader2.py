

from pathlib import Path
import json

guests = ["John", "Peter", "Mary"]
path = Path("guest.txt")

contents = json.dumps(guests)          # string like '["John", "Peter", "Mary"]'
path.write_text(contents)