def manual_count(string, count_char):
    time = 0
    for i in string:
        if i == count_char:
           time += 1
    print(f'there are {time} {count_char}, in {string}')
        

manual_count('hello world how you feeling?', 'w')