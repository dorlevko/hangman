
'''
self.py Course - Final Project

Student: Dor Levkovich
'''

import colorama
from colorama import Fore, Style


MESSAGE = '''\nplease insert:
             A) path for the file (which contain the words)
             B) index (for which word of the above file)
           '''
MAX_TRIES = 6

HANGMAN_PHOTOS = {
0: 
"""\nLet's Start!\n\nx-------x\n""",
1:
"""x-------x
|
|
|
|
|
\n""",
2:
"""x-------x
|       |
|       0
|
|
|
\n""",
3:
"""x-------x
|       |
|       0
|       |
|
|
\n""",
4:
"""x-------x
|       |
|       0
|      /|\\
|
|
\n""",
5:
"""x-------x
|       |
|       0
|      /|\\
|      /
|\n""",
6:
"""x-------x
|       |
|       0
|      /|\\
|      / \\
|\n"""               
 } 
    

def check_win(secret_word, old_letters_guessed):
    for char in secret_word:
        if char not in old_letters_guessed:
            return False
    return True 

def show_hidden_word(secret_word, old_letters_guessed):
    s = ''
    for char in secret_word:
        if char not in old_letters_guessed:
           s += ' _'
        else:
            s += ' ' + str(char)
    return s

def check_valid_input(letter_guessed, old_letters_guessed):
    if  len(letter_guessed) == 1 and 65 <= ord(letter_guessed) <= 122 \
    and letter_guessed not in old_letters_guessed:
        return True
    return False

def try_update_letter_guessed(letter_guessed, old_letter_guessed):
    letter_guessed = letter_guessed.lower()
    if check_valid_input(letter_guessed, old_letter_guessed):
        old_letter_guessed.append(letter_guessed)
        old_letter_guessed.sort()
        return True
    print('X \n%s' % ' -> '.join(old_letter_guessed))
    return False

def choose_word(file_path, index):
    index = int(index)
    file = open(str(file_path),'r')
    file_content = file.read()
    words = file_content.split(' ')
    file.close()
    return words[index]    

def welcome():
    print(Fore.LIGHTBLUE_EX + """
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                      __/ |                      
                     |___/
   
""" + Fore.RESET,MAX_TRIES)
    print(MESSAGE)



def main():
    welcome()
    file_path = input('A:')
    index = input('B:')
    secret_word = choose_word(file_path, index)
    old_letters_guessed = list()
    num_of_tries = 0
    print(HANGMAN_PHOTOS[num_of_tries],show_hidden_word(secret_word, old_letters_guessed) + "\n")
    while num_of_tries < 7:
        if check_win(secret_word, old_letters_guessed):
            print(Fore.GREEN + "WIN \nyou really good ;)" + Fore.RESET)
            exit(0)
        guess = input('please insert your guess_letter here:')
        while not try_update_letter_guessed(guess, old_letters_guessed):
            guess = input('please insert your input here:')
        if guess not in secret_word:
            print(':(\n')
            num_of_tries += 1
            if num_of_tries == MAX_TRIES:
                print(HANGMAN_PHOTOS[num_of_tries])
                print('your guess: %s' % show_hidden_word(secret_word, old_letters_guessed))
                print(Fore.RED + "LOSE" + Fore.RESET)
                exit(1)
            print(HANGMAN_PHOTOS[num_of_tries])
        print('your guess: %s' % show_hidden_word(secret_word, old_letters_guessed))
    
if __name__ == "__main__":
    main()
    