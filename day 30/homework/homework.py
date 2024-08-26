def odd_index_sum(numbers):
    total = 0
    for i in range(1, len(numbers), 2):
        total += numbers[i]
    return total

numbers = [1, 2, 3, 69, 2, 3, 69]
print(odd_index_sum(numbers))  #it will add '2' + '69' + '3' = in total thats 74 bro