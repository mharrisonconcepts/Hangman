import random 

def main():
    welcome = ["Welcome to Matt and Grace's epic hangman game!"]
    for line in welcome:
        print(line, sep='/n')
        
    playagain = True

    while playagain:
        words = ["hangman", "bathrobe", "computer", "python"]
        chosenword = random.choice(words).lower()
        playerguess = None
        guessedletters = []
        wordguessed = []
        for letter in chosenword:
            wordguessed.append("-")
        joinedword = None