import random
from words import words
import string


def get_valid_word(words):
    word = random.choice(words)
    while '_' in word or ' ' in word:
        word = random.choice(words)
    return word

def hangman():
    word = get_valid_word(words).upper()
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 9

    
    while len(word_letters)>0 and lives>0 :
        
        #letters used
        print('you have',lives,"lives left you  have used these letters",' '.join(used_letters))
        
        #what the current word is
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print("current word",' '.join(word_list))
        
        user_letter = input('\n Guess a letter: ').upper()
        if user_letter in alphabet - used_letters :
            used_letters.add(user_letter)
            if user_letter in word_letters :
                word_letters.remove(user_letter)
            else:
                lives = lives-1
                print('Letter is not in word')
        
        elif user_letter in used_letters :
            print("You have already used that charter, try again")
    
        else :
            print("you typed invalid character")
        
    if lives == 0:
        print('sorry, you die')
    else:
        print('you guessed the word',word, '!!')
        


hangman()