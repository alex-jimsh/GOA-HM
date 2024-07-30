list = [1, 2, 3, 4, 5]
last = list.pop()#no need for input cause on default it should pop last element
print(last)

str_list = ["apple", "banana", "cherry"]
first_element = str_list.pop(0)  # Removes the first element
print(first_element)  #apple

char = ['a', 'b', 'c', 'd', 'e']
element__2 = char.pop(2)
print(element__2)


empty_list = []

try:
    popped_element = empty_list.pop()  # This will raise an IndexError
except IndexError:
    print("Error: IndexError")  #Error:

int_list = [1, 5, 3, 5, 5, 7, 5, 9]
count_5 = int_list.count(5)
print(count_5)  # 4

bool_list = [True, False, True, True, False, True, False]
count_true = bool_list.count(True)
print(count_true)  #4



