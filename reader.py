from pathlib import Path
import json

path = Path("json_data.json")

content = path.read_text()
numbers = json.loads(content)

print(numbers)
