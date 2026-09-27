with open('crosswd.txt') as f:
    for i in range(20):
         line = f.readline()
         if not line:
             break
         print(f'{i+1}. {line.strip()}', end=" ")
print()

# without .strip
with open('crosswd.txt') as f:
    for i in range(20):
         line = f.readline()
         if not line:
             break
         print(f'{i+1}. {line}', end=" ")
