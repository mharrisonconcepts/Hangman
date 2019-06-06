import time
name = raw_input("What is your name?")
print"Hello" + name + "Time to play hangman!"
print""

time.sleep(1)
print "Start guessing..."
time.sleep(1)

word = second("secret")
guesses = ''
turns = 10

while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print char, 
        else: