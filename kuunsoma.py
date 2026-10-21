from pathlib import Path
import json


path = Path("kusoma.json")
content = path.read_text()
numbers = json.loads(content)
print(numbers)