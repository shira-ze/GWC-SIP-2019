import random

# A list of words that
potential_words = ["example", "words", "someone", "candy", "guess"]

word = random.choice(potential_words)

# Use to test your code:
# print(word)

# Converts the word to lowercase
word = word.lower()

# Make it a list of letters for someone to guess
current_word = list(word) #TIP: the number of letters should match the word
# print( current_word)

# Some useful variables
guesses = [] #list that holds all the previously guessed letters
maxfails = 7
fails = 0

while fails < maxfails:
    guess = input("Guess a letter: ") #guess will be a string because input always forms a string
    guess = guess.lower()
        #checks if its a letters AND(both must be true)if it is a single letter and not equal to previous guesses
    if guess.isalpha() and len(guess) == 1 and  guess not in guesses:
        #guess is single letter and current guess is new
        guesses.append(guess)
        print(f"you have so far guessed: {guesses}")
        if guess in current_word:
            print("you guessed a letter correctly!")
            #guess is right
        else:
            #guess is worng
            fails += 1
            print("you guessed incorrectly")
    else:
        print(f"invalid answer:{guess}")
        #not valid input
    print("You have " + str(maxfails - fails) + " tries left!")

    #
    display = ""
    winning = ""
    for i in current_word:
        if i in guesses:
            display += i + ""
            winning += i #display without the spaces, and only updated for correct guess, so winning can == word 100% without the extra wrong guesses
                    #print(i)
        else:
            display += "_ "
            #print("_")
    print(display)
    if winning == word:
        print("you won")
        exit(0)




print(f"you have lost, the word was {word}")
