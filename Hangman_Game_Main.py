import random
from words import word_list

def get_word():
    word=random.choice(word_list)
    return word.upper()


def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


def play(word):
    word_completion='_'*len(word)
    #print(word)
    guessed_letters=[]
    guessed_words=[]
    guessed=False
    chances=6

    print(display_hangman(chances))
    print(word_completion)
    print('\n')
    while not guessed and chances >0 :
        guess=input('Please guess a letter or word: ').upper()

        if len(guess) ==1 and guess.isalpha():
            if guess in guessed_letters:
                print('You have already guessed the letter ', guess)
                print("Guessed Letters :  " ,guessed_letters)
            elif guess not in word:
                print(guess, "is not in the word.")

                chances -= 1
                guessed_letters.append(guess)
                print("Guessed Letters :  ", guessed_letters)

            else:
                guessed_letters.append(guess)
                print('Good job,' + guess + '  is in the word!')
                print("Guessed Letters :  ", guessed_letters)
                word_as_list=list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
                print("Guessed words :  ", guessed_words)
            elif guess != word:
                print(guess, "is not the word.")
                chances -= 1
                guessed_words.append(guess)
                print("Guessed words :  ", guessed_words)
            else:
                guessed = True
                word_completion = word
        else:
            print('Is not a valid guess')
        print(display_hangman(chances))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")





name=input("""#########################################################################
Welcome to the Hangman Game! Please Enter your Preferred game Name:     
""")
print("""Hi!""", name.upper(), """Glad to have you here!
You will be playing against the computer today
The computer will randomly choose a word and you will try to guess what the word is.
###############################################
Good Luck! Have fun Playing :)""")
w=get_word()
play(w)
while input("Play Again? (Y/N) ").upper() == "Y":
    word = get_word()
    play(word)







