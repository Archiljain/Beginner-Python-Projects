import random
# # options = [ "Draw", "win", "lose",
# #             "lose", "Draw", "win",
# #             "win", "lose", "Draw"  ]
print("\n ===Snake,Water & Gun=== \n")
print("\n 0. snake")
print("\n 1. Water")
print("\n 2. Gun")
def check(comp, user):
    if (comp == user):
        return 0
    if comp == '2' and user == '0':
        return -1
    if (comp == '0' and user == '1'):
        return -1
    if (comp == '1' and user == '2'):
        return -1
    else:
        return 1
user = input("choose option between (0-2):")
comp = random.randint(0, 2)

score = check(comp, user)
print("You:", user)
print("computer:", comp)

if (score == 0):
    print("Draw")
elif (score == -1):
    print("You lose")
elif(score == 1):
    print("You win!")





