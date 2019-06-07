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
        
        attempts = 10
        
        while (attempts !0 and "-" in wordguessed):
            print(("\nYou have {} attempts remaining").format(attempts))
            joinedword = "".join(wordguessed)
            print(joinedword)
            
            try:
                playerguess = str(input("\nPlease select a letter between A-Z"))
            except:
                print("That is not valid input. Please try again.")
                continue
            else: 
                if not playerguess.isalpha(): 
                    print("That is not a letter. Please try again.")
                    continue
                elif len(playerguess) > 1:
                    print("That is more than one letter. Please try again")
                    continue
                elif playerguess in guessedletters: 
                    print("You have already guessed that letter. Please try again.")
                    continue
                