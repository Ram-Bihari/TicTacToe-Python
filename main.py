import random

name = input('Enter your name ')
print('Ahh I have been expecting u', name)
print('So do u wanna play a game of rock paper scissors? YOU DON\'T HAVE A CHOICE!')

comp_choice = ['rock', 'paper', 'scissors']
choice = input('I have decided my move. What about you? ')  
random_choice = random.choice(comp_choice)

if choice.lower() == 'rock' and random_choice == 'paper':
  print('Computer: Paper               Sid: Rock')
  print('HAHA! I WON! LOSER!!')
elif choice.lower() == 'paper' and random_choice == 'scissors':
  print('Computer: Scissors               Sid: Paper')
  print('HAHA! I WON DUDE! YOU ARE THE BIGGEST NOOB I\'VE EVER SEEN. GO WATCH CHOTTA BHEEM')
elif choice.lower() == 'scissors' and random_choice == 'rock':
  print('Computer: Rock               Sid: Scissors')
  print('BYE BYE! GO AND WATCH TIKTOK!')
elif random_choice == 'rock' and choice.lower() == 'paper':
  print('Computer: Rock               Sid: Paper')
  print('U KNOW, I LET PEOPLE WIN SO THAT THEY DON\'T FEEL BAD')
elif random_choice == 'paper' and choice.lower() == 'scissors':
  print('Computer: Paper               Sid: Scissors')
  print('NO COMMENTS!')
elif random_choice == 'scissors' and choice.lower() == 'rock':
  print('Computer: Scissors               Sid: Rock')
  print('YEAH WHATEVER!')
elif random_choice == 'rock' and choice.lower() == 'rock':
  print('Computer: Rock               Sid: Rock')
  print('TIE!')
elif random_choice == 'paper' and choice.lower() == 'paper':
  print('Computer: Paper               Sid: Paper')
  print('TIE!')
elif random_choice == 'scissors' and choice.lower() == 'scissors':
  print('Computer: Scissors               Sid: Scissors')
  print('TIE!')

print('GG!')



