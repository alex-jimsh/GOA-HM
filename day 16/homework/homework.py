# 1)
family_members = ["nika", "leqso", "niga", "biga"]
for i in range(len(family_members)):
    print(family_members[i])

# 2)
numbers_1_to_10 = list(range(1, 11))
print("First element:", numbers_1_to_10[0])
print("Last element:", numbers_1_to_10[-1])

# 3)
numbers_10_to_20 = list(range(10, 21))
for i in range(0, len(numbers_10_to_20), 2):
    numbers_10_to_20[i] = 1
print(numbers_10_to_20)

# 4)
name = input("Enter your name: ")
surname = input("Enter your surname: ")
age = input("Enter your age: ")
residence = input("Enter your residence: ")


user_info = [name, surname, age, residence]
print(user_info)

# 5)
surname = "zangadze"
for i in range(len(surname)):
    print(surname[i])
