print("Welcome to Love Calculator!")

name1 = input("What is your name?\n")
name2 = input("What is their name?\n")

combined_names = str(name1).lower() + str(name2).lower()

t = combined_names.count("t")
r = combined_names.count("r")
u = combined_names.count("u")
e = combined_names.count("e")

l = combined_names.count("l")
o = combined_names.count("o")
v = combined_names.count("v")
e = combined_names.count("e")

true = t + r + u + e
love = l + o + v + e

true_love = int(str(true) + str(love))

if true_love < 10 and true_love > 90:
    print(f"Your love score is {true_love}. You guys are like Water and Fire.")
elif true_love > 40 and true_love < 50:
    print(f"Your love score is {true_love}. You are alright together.")
else:
    print(f"Your love score is {true_love}.")
