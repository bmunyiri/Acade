from pathlib import Path

guest_list = []
while True:
    guest_name = input("Your name please (or type q to quit): ").strip()
    if guest_name.lower() == "q":
        break
    if guest_name:              # skip empty input
        guest_list.append(guest_name)

path = Path("guest.txt")
path.write_text("\n".join(guest_list) + "\n")
print(f"Wrote {len(guest_list)} guests to {path.resolve()}")
