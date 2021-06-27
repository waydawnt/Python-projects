import random

rock = '''    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)'''

scissor = '''    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''

map = [rock, paper, scissor]

print("What's your choice?")
choices = input("1 = Rock, 2 = Paper, 3 = Scissor : ")
user_choice = int(choices) - 1
computer_choice = random.randint(0,2)

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You Lose!")
else :
    print(f"Your Choice :\n{map[user_choice]}")
    print(f"Computer's Choice :\n{map[computer_choice]}")

    if user_choice == 0 and computer_choice == 2 :
        print("You Win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You Lose!")
    elif computer_choice > user_choice :
        print("You Lose!")
    elif computer_choice < user_choice :
        print("You Win!")
    elif computer_choice == user_choice :
        print("It's Draw!")