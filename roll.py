import random


# roll a "die" some number of times.

# roll - run it once and go into a loop
# roll 1 - produce a number 1-6 random and print it
# roll 2 - produce two numbers 1-6 and print them
# roll 3 - produce three numbers and print them.
#
def game():
    play_again = True
    while play_again:
        list = []
        x = input("How may times would you like to roll?: \n")
        for i in range(int(x)):
            d = int(random.randrange(1, 7))
            list.append(d)
        print("you rolled... "+str(list))
        p = input("If you want to play again press 'Enter' if not press 'N' \n")
        if p == 'N':
            play_again = False


        # continue






game()
