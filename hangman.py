import random
wordList= ["orangee", "banana", "apple", "pear", "strawberry", "watermelon", "kiwi", "grape", "blueberry", "plum" ]
secretWord = random.choice(wordList)
hiddenWord = "_"*len(secretWord)
secretWordList = (list(secretWord))
hiddenWordList = (list(hiddenWord))


def switching(userLetter):
    hiddenWord=""
    i = 0
    while i < len(secretWordList):
        if secretWordList[i] == userLetter:
            hiddenWordList[i] = userLetter
        i = i + 1  
    
    
    

def winning():
    print("Congratulations! You saved the fruit")
    


def hangman():
    i = 0
    print(hiddenWord)
    while i < 7:
        n=""        
        userLetter = input("Pick a letter. ").lower()
        if secretWordList.count(userLetter) > 0:
            switching(userLetter)
            n = n.join(hiddenWordList)
            print(n)
            if hiddenWordList.count("_") == 0:
                winning() 
                break
        else:
            print("Wrong")
            n = n.join(hiddenWordList)
            print(n)
            i = i + 1
        print("="*30)
    if i == 7:
        print("Your fruit rott. The correct answer was " + secretWord)

print("You lost your fruit. Guess it before it rots.")
hangman()