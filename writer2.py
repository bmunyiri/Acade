
with open("kusoma.csv") as file:
    people = []
    for line in file:
        name, movie = line.strip().split(",")
        people.append({"name": name, "movie": movie})

    # print formatted strings sorted by name
    for p in sorted(people, key=lambda x: x["name"]):
        print(f"person {p['name']} like the movie {p['movie']}")

    # print sorted by movie
    for p in sorted(people, key=lambda x: x["movie"]):
        print(p)
