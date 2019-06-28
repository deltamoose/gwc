import random

print("Welcome to Hangman!  ")
user = input("What is your name?  ")
play = input("Welcome to Hangman, " + user + ".  Type 'start' to begin the game.  ")


if play == "start":
    secretWord = ['banana', 'preposterous', 'lucrative', 'enigma', 'apple']
    word = random.choice(secretWord)
    # print(word)
else:
    print("Maybe next time!")
    quit()

guess = input

if word == "banana":
    print("the word has 6 letters")
    banana = ['b', 'a', 'n', 'a', 'n', 'a']
    if guess == letter:
        print("Correct!  " + user + " picked" + guess)
if word == "preposterous":
    print("the word has 12 letters")
    preposterous = ['p', 'r', 'e', 'p', 'o', 's', 't', 'e', 'r', 'o', 'u', 's']
    if guess == letter:
        print("Correct!  " + user + " picked" + guess)
if word == "lucrative":
    print("the word has 9 letters")
    lucrative = ['l', 'u', 'c', 'r', 'a', 't', 'i', 'v', 'e']
    guess = input("Guess a letter (a-z).  ")
    for letter in range (0-9):
        def lucrative[0]
    if guess == letter:
        print("Correct!  " + user + " picked" + guess)
if word == "enigma":
    print("the word has 6 letters")
    enigma = ['e', 'n', 'i', 'g', 'm', 'a']
    if guess == letter:
        print("Correct!  " + user + " picked" + guess)
if word == "apple":
    print("the word has 5 letters")
    apple = ["a", 'p', 'p', 'l', 'e']
    if guess == letter:
        print("Correct!  " + user + " picked" + guess)


dash = '_ ' * len(word)
print (dash)
print (word)

guesses = []
maxfails = 12
fails = 0

while fails > maxfails:
    guess = input("Guess a letter: ")
    print(guess)
    print (guess in word)

    print(current_word)

    fails = fails + 1
    print("You have " + str(maxfails - fails) + " more tries")
