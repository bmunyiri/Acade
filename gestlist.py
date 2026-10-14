from tkinter import messagebox

guests = ['john', 'joseph','mary']

for i in range(len(guests)):
    print(f"Dear {guests[i]} , you are invited to my Christmas party")

for guest in guests:
    print( f'Dear {guest} , you are invited to my Christmas parry-, ')

age =int(input("Enter your age: "))

if age < 2:
    stage = "baby"
elif 2 <= age < 4:
    stage = "toddler"
elif 4 <= age < 13:
    stage = "kid"
elif 13 <= age < 20:
    stage = "teenage"
elif 20 <= age < 65:
    stage = "adult"
else:
    stage = "elder"

print(f'According to your age, you are classified as {stage}')

#-----------------------------------------
