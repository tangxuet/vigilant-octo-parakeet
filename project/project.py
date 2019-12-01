import os
import csv
import random
HANGMANPICS = ['''
    +---+
    |   |
        |
        |
        |
        |
  =========''', '''
    +---+
    |   |
    O   |
        |
        |
        |
  =========''', ''' 
    +---+
    |   |
    O   |
    |   |
        |
        |
  =========''', '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
  =========''', '''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
  =========''', ''' 
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
  =========''', '''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
  =========''']  # the images of hangman are copied from other works https://inventwithpython.com/chapter9.html


def show_word_progress(letter_guess,the_word):
    # used to show the underline to represent word haven't been guessed
    word_shown = ''
    for i in the_word:
        if i == letter_guess or i in l:
            word_shown = word_shown + i    
        else:
            word_shown = word_shown + ' _'
    print(word_shown) 

def write_own_list():
    # create user's own list
    another = 'yes'
    while another == 'yes':
        key = input('What is your wordlist name? ==> ')
        l = []
        i = ''
        while i != 'stop':
            l.append(i)
            i = input("Please type the new word, 'stop' to finnish: ")
        l.pop(0)
        d[key] = l
        print(key + ' has been created!')
        another = input('Do you wanna create another wordlist? yes/no ==> ')
    
        
d = {} # empty set to restore new word list
print('''
                    [[[ H  A  N  G  M  A  N ]]]           ''')
print('''
                              +---+
                              |   |
                              O   |
                             /|\  |
                             / \  |
                                  |
                             =========''')
start_button = input('''
Please type 'start' to start the game 
type 'create own word list' to add your own word list ==> ''')
while start_button == 'create own word list':   
    write_own_list()
    start_button = input('''Please type 'start' to start the game ==> ''') 
    
while start_button == 'start' or start_button == 'resume':
    i = os.system('cls')
    print('''
                        [[[ H  A  N  G  M  A  N ]]]           ''')
    print('''
                                  +---+
                                  |   |
                                  O   |
                                 /|\  |
                                 / \  |
                                      |
                                 =========''')    
    if start_button == 'resume':
        ask = input("Do you wanna make new word list? Yes/No ==> ")
        if ask == "Yes":
            write_own_list()    
    mode = input('''Choose the word list: 'own word list' or 'game word list' ==> ''')
    if mode == 'own word list':
        if d == {}:
            print("You haven't make your own word list!!! You can use Game wordlist this time!" )
            mode = 'game word list'
        else:
            listname = input('please type your word list name: ')
            while not listname in d:
                listname = input("It's not an existing list! type again: ")
            if listname in d:
                word_list = d[listname]
                
    
    if mode == 'game word list':
        level = input('''Please choose game difficulty: easy/hard ==> ''')
        while not(level == 'easy' or level == 'hard'):
            level = input('''Please choose game difficulty: easy/hard ==> ''')
        if(level == 'easy'):
            word_base = open("easy.csv","r")
            reader = csv.reader(word_base)
        elif(level == 'hard'):
            word_base = open("hard.csv","r")
            reader = csv.reader(word_base)
        big_list = list(reader)
        word_base.close()
        word_list = []
        for i in range(len(big_list)):
            word_list = word_list + big_list[i]
        

    word = random.choice(word_list)
    print('There is ' + str(len(word)) + ' letters in this word~')
    blank = ''
    for i in range(len(word)):
        blank = blank + '_ '
    print(blank)
    chance = 7
    num_word = len(word)
    num_word_left = len(word)
    l = []
    while chance > 0 and num_word_left > 0:
        num_letter = 0
        letter = input('Can you guess a letter? ==> ')
        for index in range(len(word)):
            if (word[index] == letter):
                num_letter = num_letter + 1
        if (num_letter > 0) and (not letter in l):
            num_word_left = num_word_left - num_letter
            print("good job! there's " + str(num_word_left) + " letters left.")
            l.append(letter)
            show_word_progress(letter,word)
        elif (num_letter == 0):
            show_word_progress(letter,word)
            chance = chance - 1
            print('guess failed, ' + str(chance) + ' chances left.')
            print(HANGMANPICS[6 - chance])
        else:
            print(letter + ' has already been guessed.')
        
    if (num_word_left == 0):
        print('Congradualations! The word is ' + word + '.')
    if (int(chance) == 0):
        print('No chance left, you failed!!!')
        answer = input('Do you wanna know the answer? yes/no')
        if answer == 'yes':
            print(word)
        if answer != 'yes':
            print('Bye Bye~')
    start_button = input('''Type resume to start again ==> ''')