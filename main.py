import art
print(art.logo)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input('You\'re at a crossroad, where do you want to go? '
      'Type "right" or "left".\n').lower()
if choice1 == "left":
    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake.'
                    'Type "wait" to wait for a boat.'
                    'Type "swim" to swim across.\n').lower()
    if choice2 == "wait":
        choice3 = input('You arrive at the island unharmed.'
                        'There is the house with 3 doors. One "red", '
                        'one "yellow" and one "blue".'
                        'Which door do you choose?\n').lower()
        if choice3 == "red":
            print("It's a room full of fire. Game Over!")
        elif choice3 == 'yellow':
            print("You found the treasure. You Win!")
        elif choice3 == 'blue':
            print("You entered a room of beats. Game Over!")
        else:
            print("You chose a door that doesn't exist. Game Over!")
    else:
        print("You got attacked by angry trout. Game Over!")
else:
    print("You fell into a hole. Game Over")