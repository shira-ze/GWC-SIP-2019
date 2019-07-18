answer = input ("Player one: pick a word")


word = (answer)
word = word.lower()
wordList = list(word)

currentWord = "_" * len(word)
currentWord_list = list(currentWord)

tries = 6

while(tries > 0):
    guess = input("Guess a letter for the word i'm thinking of! ")
    guess = guess.lower()

    if(guess in wordList):
        index1 = wordList.index(guess)
        currentWord_list[index1] = guess

        tries -= 1
        print(currentWord_list)

if tries == 6:
    print("Game Over!")
