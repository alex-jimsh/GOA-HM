print('insert random amount')
x = int(input())
print('second one please')
y = int(input())
print('now what would u like to do with your numbers')
print('options: /, *, -, +,')
print('choose one')
answer = input()
if answer == "/":
    print(x / y)
elif answer == "-":
    print(x - y)
elif answer == "+":
    print(x + y)
elif answer == "*":
    print(x * y)