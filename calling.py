
count = 0
with open("guest.txt") as reading_object:
    for lines in reading_object:
        print(lines.strip())
        count += 1





print(f"there are { count} lines of data")