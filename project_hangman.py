#Project Hangman
from os import system
from random import choice
from time import sleep

def randomcolor():
    while(True):
        c1=str(choice("0123456789ABCDEF"))
        c2=str(choice("0123456789ABCDEF"))
        if c1!=c2:
            colorcode ='color '+c1+c2
            system(colorcode)
            break
VERSION='0.2-alpha'
print('\t\t Welcome to Hangman '+VERSION)
print('\nCopyright (C) 2020 Aditya Anand - All Rights Reserved. You may use, distribute and modify this code under the terms of the GNU General Public License v3.0\n')
print('Source code can be found here. https://github.com/mark-IV-II/Project_hangman.git\n')
dictionary=(open(r'dictionary4hangman.txt').readlines())

replay=True
while(replay):
    word=(choice(dictionary).strip())
    word_length=len(word)
    ans=[]
    missed=[]
    if word_length>5:
        attempts=10
    else:
        attempts=6
    print('\nThe word has ',word_length,' alphabets and you have ',attempts,' attempts to guess it. Enjoy!!\n')
    randomcolor()
    sleep(2)
    for i in range(0,word_length):
        ans.append('_')
    while(attempts>=0):
        print(*ans, sep=' ')
        print('Misfires: ',missed)
        if attempts==0:
            print('\n Sorry, you have exhausted your attempts. The word was '+ word)
            break
        char=input('\nEnter your guess\n')
        if len(char)>1:
            print('\nOnly one alphabet is allowed at a time. Please try again\n')
            sleep(0.75)
            continue
        elif char not in word:
            attempts-=1
            missed.append(char)
            print('Missed attempt. '+str(attempts)+' attempt(s) left\n') 
            sleep(0.68)
            continue
        elif char in word :
            for i in range(0,word_length):
                if word[i]==char:
                    ans[i]=char
        if '_' not in ans:
            print('Congratulations. You have guessed the word \n \t'+word)
            break
    replay_prompt=input('Do you like to play again (Y/N)\n')
    if replay_prompt.lower()=='n':
        replay=False

print('\n\t\t Thank you for playing Hangman')
sleep(2)
