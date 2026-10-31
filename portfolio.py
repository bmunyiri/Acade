filename = "portfolio.csv"

listing=[]
with open(filename) as f:
    next(f)  # Skip the header line
    for lines in f:
        row = lines.strip().split(",")
        name = row[0]
        shares = int(row[1])
        price =float(row[2])
        listing.append((name,shares,price))

print(listing)


#Better way of programming==============================================

import csv

listing = []
with open(filename, newline="") as f:
    reader = csv.DictReader(f, skipinitialspace=True)   # skipinitialspace trims " shares" -> "shares"
    for row in reader:
        listing.append((
            row["name"].strip(),
            int(row["shares"]),
            float(row["price"]),
        ))

print(listing)

