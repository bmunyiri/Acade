bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[2].title())
message = f'my first bicycle was a {bicycles[0].title()}'
print(message)

names = ['joanina', 'moses', 'jane']
print(names[0].title())
print(names[1].upper())
message2 = 'Greatings from earth '
print(message2, names[0])

names.append('peter')
print(names)
names[1]='mohammed'
print(names)
names.insert(0,'rosemary')
print(names)
del names[0]
print(names)

poped_name = names.pop()
print(names)
print(poped_name)
print(poped_name.title())

not_a_good_friend = names[1]
names.remove(not_a_good_friend)
print(f'i hard to remove {not_a_good_friend} , for being nasty')
print(names)

pizzas = ["mushrooms","pinaple", "peporoni" ]
for pizza in pizzas:
    print(f"i like {pizza} pizza" )


