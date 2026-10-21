from pathlib import Path

guests = ["John", "Peter", "Mary"]
Path("guest.txt").write_text("\n".join(guests)) #If you want one guest per line instead (not JSON)
