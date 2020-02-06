# More on loops

# Basic FOR loop
import random

for i in range(5, 51, 5):
    print(i, end=" ")
print()
# RANGE function (alternative for comprehension)
my_list = [x for x in range(100)]
print(my_list)

my_list = list(range(100))  # iterable
print(my_list)

# BREAK (breaks out of the loop)
for number in my_list:
    if number > 10:
        break
    print(number, end=" ")

print("End of loop")

# CONTINUE (skips to the end of the loop for that iteration)
for number in my_list:
    if number % 7 == 0:
        continue
    print(number, end=" ")


# FOR ELSE
for number in my_list:
    print(number, end=" ")
    if number == 80:
        break
else:
    print("The loop completed naturally")

print()


# Add me as a collaborator on Github




# HANGMAN HELP!!!
# grabbing a random word from a list
my_list = ["APPLE", "BANANA", "CHERRY", "DONUT"]

# first way
random.shuffle(my_list)
my_word = my_list.pop()
print(my_word, my_list)

# second way
my_word = my_list.pop(random.randrange(len(my_list)))
print(my_word, my_list)

used_letters = ["A", "S", "T"]
my_word = "GHOST"


# game loop

# make a list of words
# pick a random word
done = False
while not done:
    # print the gallows
    # print the word with blanks or letters
    correct = True
    for letter in my_word:
        if letter in used_letters:
            print(letter, end=" ")
        else:
            print("_", end=" ")
            correct = False

    guess = input("Pick a letter")
    # check to see if already selected
    # check if in word (if it isn't, you lose a life)
    # check for a win or loss






