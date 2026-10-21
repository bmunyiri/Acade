with open("kusoma.csv") as file:
    for line in file:
        name,movie = line.strip().split(",")


        print(f"name :{name} movie :{movie}")

