# More on LOOPS

# Basic FOR loop
import random

for i in range(5, 51, 5):
    print(i, end=" ")
print()

# RANGE function (alternative for comprehension)
my_list = [x for x in range(1, 101)]
print(my_list)

my_list = list(range(1, 101))
print(my_list)

# BREAK
for number in my_list:
    print(number)
    if number > 10:
        break  # forces out of nearest loop

# CONTINUE
for number in my_list:
    if number % 7 == 0:
        continue  # skips the rest of this iteration
    print(number)


# FOR ELSE
for number in my_list:
    if number == 200:
        print("You UNnaturally finished the loop")
        break
    print(number)
else:
    print("You naturally finished the loop")


# Add me as a collaborator on Github



# HANGMAN HELP!!!


# game loop
# make a list of words
# pick a random word
my_list = ["APPLE", "BANANA", "CHERRY", "DRAGONFRUIT"]
my_word = my_list.pop(random.randrange(len(my_list)))
print(my_word, my_list)

# another way to get the random word
random.shuffle(my_list)
my_word = my_list.pop()
print(my_word, my_list)

done = False
used_letters = ["A", "R"]
number_missed = 0

while not done:
    # print the gallows
    # print the word with blanks or letters
    for letter in my_word:
        if letter in used_letters:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print()

    guess = input("Pick a letter")
    # check to see if already selected
    # check if in word (if it isn't, you lose a life)
    # check for a win or loss