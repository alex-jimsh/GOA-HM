print('wassup please insert your name:')
def greet(name):
    return "Hello, " + name + ' how you been its pleasure to see you'
print(greet(input()))

print('alright, now why dont u tell my your family members age and i will tell you how old they will be in 20 years')
print("let's go with grandpa insert his age")
def grandpa(age):
    return age + 20
print(grandpa(int(input())))
print("let's go with grandma insert his age")
def grandma(age):
    return age + 20
print(grandma(int(input())))
print("let's go with father insert his age")
def father(age):
    return age + 20
print(father(int(input())))
print("let's go with mother insert his age")
def mother(age):
    return age + 20
print(mother(int(input())))

print('now insert your, name: lastname: address: gmail: follow the order')
def info(name,lastname,address,gmail):
    return "so your name is " + name + 'your last name is ' + lastname + " and your live in  " + address + ' and your gmail is ' + gmail

print(info(input(), input(), input(), input()))

