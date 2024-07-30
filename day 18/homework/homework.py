person = {'name' : 'alex', 'age' : 17, 'city' : 'tbilisi', 'work' : 'unemployed'}
print(f"my name is {person['name']}, i am {person['age']} years old, i live in {person['city']}, and right now i am {person['work']} ")
schoolbook = {'math' : 10, 'english' : 9, 'georgian' : 9, 'physichs' : 8}
x = schoolbook['math'] + schoolbook['english'] + schoolbook['georgian'] + schoolbook['physichs']
print(x / 4)
print('is your whole years grade good joob')
book = {'edgarpoe' : 'The pit and the pendulum', 'dostoevsky' : 'crime and punishment', 'thomas harris' : 'silence of the lambs', 'akutagawa' : 'the life of a stupid man'}
print(f"let me intoduce you to my favorite books first one {book['edgarpoe']} by edgar poe, second one is {book['dostoevsky']} by dostoevsky")
print(f'lets go with 3rd one and its one of the books and movie that really got me in {book['thomas harris']} itself the legend ')
print(f'and the last one gotta go to {book["akutagawa"]} by akutagawa japanese author beautiful book involving 3 stories of a stupid man')

print('now lets go shopping shell we, what would u like to buy first ?')
shoppinglist = {}
shoppinglist['item 1'] = input()
print('okay, want anything else?')
answer = input()
if answer == 'no':
    print(shoppinglist)
else:
  print('okay whats it going to be?')
  shoppinglist['item 2'] = input()
  print('anything else?')
  answer1 = input()
  if answer == 'no':
     print(shoppinglist)
     print('thats all you got bye!!')
  else:
     print('okay whats it going to be?')
     shoppinglist['item 3'] = input()
     print(shoppinglist)
     print('okay please now leave!!!')
  
