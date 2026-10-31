year, numyears = 1, 10
principal, rate = 1000.0, 0.05

with open('out.txt', 'w') as out:
    while year <= numyears:
        principal = principal * (1 + rate)
        print(f'{year:>3d} {principal:0.2f}', file=out)
        year += 1