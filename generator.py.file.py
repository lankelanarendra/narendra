def display():
    x="good morning"
    b=x.upper()
    print('nani',end=" ")
    yield b
    c=x.lower()
    print('narendra',end=" ")
    yield c
    d=x.capitalize()
    print("naveeen",end=" ")
    yield d
a=display()
print(a)
print(next(a))
print(next(a))
print(next(a))