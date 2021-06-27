import random

print("Welcome to Random Name Picker!")
names_string = input("Give me everybody's name, seperated by comma : ")
names = names_string.split(", ")

print(names[random.randint(0, (len(names) - 1))])