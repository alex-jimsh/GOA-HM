def manual_count(string, count_char):
    time = 0
    for i in string:
        i = count_char
        print(f'there are {time} {count_char}, in {string}')
        break

manual_count('hello world how you feeling?', 'o')