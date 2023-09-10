while True:
  print()
  ask = input('What animal do you want: ').lower()
  print()
  if ask == 'cat':
    print(f'A {ask} goes meow ')
    print()
    exit = input('Do you want to play again? y/n: ')
    if exit == 'n':
      break
    else:
      continue
  elif ask == 'horse':
    print()
    print(f'A {ask} goes neigh ')
    print()
    exit = input('Do you want to play again?: ')
    if exit == 'n':
      break
    else:
      continue
  elif ask == 'dog':
    print()
    print(f'A {ask} goes meow ')
    print()
    exit = input('Do you want to play again?: ')
    if exit == 'n':
      break
    else: 
      continue
  elif ask == 'goat' or ask == 'sheep':
    print()
    print(f'A {ask} goes baa')
    print()
    exit = input('Do you want to play again?: ')
    if exit == 'n':
      break
    else:
      continue
  elif ask == 'bird' or ask == 'cricket':
    print()
    print(f'A {ask} chirps !')
    print()
    exit = input('Do you want to play again?: ')
    if exit == 'n':
      break
    else:
      continue    
  elif ask == 'lion':
    print()
    print(f'A {ask} roars and it is very dreadful !')
    print()
    exit = input('Do you want to play again?: ')
    if exit == 'n':
      break
    else:
      continue    
  elif ask == 'mosquitoe':
    print()
    print(f'A {ask} goes buzz !')
    print()
    exit = input('Do you want to play again?: ')
    if exit == 'n':
      break
    else:
      continue    