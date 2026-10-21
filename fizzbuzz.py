
def fizz_buzz(name: int):
    if (name % 3 == 0) and (name % 5 == 0):
        print("FizzBuzz")
    elif name % 3 == 0:
        print("Fizz")
    elif name % 5 == 0:
        print("Buzz")
    else:
        print(name)

fizz_buzz(115)


#=============================================================
def fizz_buzz(name: int):
    if name % 15 == 0:
        print("FizzBuzz")
        return
    if name % 3 == 0:
        print("Fizz")
        return
    if name % 5 == 0:
        print("Buzz")
        return
    print(name)




