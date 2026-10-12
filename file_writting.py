from pathlib import Path
import json

limeup = ["1","2","3","5"]

path = Path("json_data.json")

content = json.dumps(limeup)
path.write_text(content)

print(content)


