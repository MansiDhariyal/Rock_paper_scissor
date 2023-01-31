rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
all=[rock,paper,scissors]
num1=int(input("Type 0 for rock, 1 for paper and 2 for scissors:"))
num2=random.randint(0,2)
if num1>=3 or num1<0:
  print("You typed invalid number.PLease try again!")
else:
  print("You choose:")
  print(all[num1])
  print("Computer choose:")
  print(all[num2])
  if num1>num2:
    print("You won")
  elif num1<num2:
    print("you loose")
  else:
    print("Its a tie")
