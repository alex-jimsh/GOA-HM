#1
def is_divisible(n, x, y):
    return n % x == 0 and n % y == 0

#2
def array_plus_array(arr1, arr2):
    return sum(arr1) + sum(arr2)

#3
def feast(beast, dish):
    return beast[0] + beast[-1] == dish[0] + dish[-1]

#4
def say_hello(name, city, state):
    name1 = ' '.join(name)
    return f"Hello, {name1}! Welcome to {city}, {state}!"

#5
def points(games):
    score = 0
    for game in games:
        x, y = map(int, game.split(':'))
        if x > y:
            score += 3
        elif x == y:
            score += 1
    return score


