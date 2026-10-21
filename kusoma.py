from pathlib import Path
import json

numbers = ["kuku","panya"]

path = Path("kusoma.json")
content = json.dumps(numbers)
path.write_text(content)
