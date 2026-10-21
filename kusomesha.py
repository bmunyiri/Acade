from pathlib import Path
import json

passenger = input("What if your name ?: ")

path = Path("kusoma.json")
content = path.read_text()
passengers = json.loads(content)
if passenger in passengers:
    print(f"Welcome back {passenger} , we are happy to have you back")
else:
    path = Path("kusoma.json")
    content = json.dumps(passenger)
    path.write_text(content)
    print(f"We will remember you  {passenger} , when you come back")

    # TODO: not to over write

