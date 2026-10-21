
with open("kusoma.csv") as file:
    for line in file:
        name, address = line.strip()
        print(f"Name : {name}, Address : {address}")
            