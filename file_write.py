
from pathlib import Path
import json

numbers =[1,2,3,45,56,67,7]

path = Path("data_file.json")
content = json.dumps(numbers)
path.write_text(content)


