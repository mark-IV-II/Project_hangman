#This script uses only modules/packages from default python installation, ie, no third party modules were used to build this

import sys
import tkinter
from random import choice
from tkinter import messagebox



 
class parameters:

    def __init__(self):

        self.word=''
        self.attempts=0
        self.output=[]
        self.missed=''
        self.score=0

    def choose_word(self):

        dictionary=(open(r'dictionary4hangman.txt').readlines())
        self.word=(choice(dictionary).strip())
        self.word=self.word.upper()
        return self.word
    
    def retrieve_word(self):
        print(self.word)
        return self.word

    def generate_output(self,word):
        self.output=[]
        self.output=['__  ' for i in word]

    def update_output(self,ans):
        self.output=ans
    
    def retrieve_output(self):
        return self.output

    def retrieve_output_string(self):
        return ''.join(self.output)

def start():

    word=params.choose_word()
    print(word)
    params.generate_output(word)
    params.missed=''
    params.score=0
    calculate_attempts(word)
    display_all_elements()

def reset():
    
    word=params.choose_word()
    print(word)
    params.generate_output(word)
    params.missed=''
    calculate_attempts(word)
    display_all_elements()
    messagebox.showinfo('Nice','A new word has been selected')

def quit_game():

    score_line='Thank you for playing Hangman. Your score is '+str(params.score)
    messagebox.showinfo('Thank You',score_line)
    sys.exit()


def calculate_attempts(word):

    if len(word)>5:params.attempts=10

    else:params.attempts=6


def check_ans(event=None):

    print('checking')
    char=str(input_box.get())
    print('input retrieved',char)
    word=params.retrieve_word()
    print('word retrieved',word)
    word_length=len(word)
    ans=params.retrieve_output()
    print('output retrieved',ans)

    if len(char)==1:

        if not char.isalpha():

            messagebox.showwarning('Oops', 'You have entered an invalid charactor. Please try again')
            display_all_elements()
            return None

        else:
            
            char=char.upper()

            if char not in word:

                params.attempts-=1

                if params.attempts==0:

                    score_line='Oops, you have exhausted your attempts. Your score is '+str(params.score)
                    messagebox.showinfo('Game Over',score_line)
                    start()
                    display_all_elements()
                    return None
                    
                params.score-=1
                params.missed+=(char+',')
    
            if char in word and char not in ans :

                for i in range(0,word_length):

                    if word[i]==char:

                        ans[i]=char
                        params.score+=2
                        
                params.update_output(ans)
                print(params.retrieve_output_string())
                if params.retrieve_output_string()==word:

                            celebration_line='You have guessed the word '+params.retrieve_word()
                            messagebox.showinfo('Congratulations', celebration_line)
                            params.score+=5
                            reset()
                
    else:
        messagebox.showwarning('Uh oh','Only one alphabet is allowed at a time. Please try again')
        

    display_all_elements()

def display_all_elements():

    input_box.delete(0,'end')

    attempt_box.delete(0,'end')
    attempt_box.insert(0,str(params.attempts))

    score_box.delete(0,'end')
    score_box.insert(0,str(params.score))

    output_box.delete(0,'end')
    output_box.insert(0,str(params.retrieve_output_string()))

    missed_box.delete(0,'end')
    missed_box.insert(0,str(params.missed))  



VERSION='v0.3-alpha'
title_line='Hangman '+VERSION
welcome_line='Welcome to Hangman '+VERSION

root=tkinter.Tk()
root.title(title_line)
root.bind('<Return>',check_ans)
game_canvas=tkinter.Canvas(root, width = 800, height = 450)
game_canvas.pack()

welcome_label=tkinter.Label(root, text=welcome_line)
welcome_label.config(font=('verdana',16))
attempt_label=tkinter.Label(root, text='Attempts left')
score_label=tkinter.Label(root, text='Score')
output_label=tkinter.Label(root, text='The word to guess is : ')
output_label.config(font=('comic sans',14))
input_label=tkinter.Label(root, text='Enter your guess')
missed_label=tkinter.Label(root, text='Misfires')
source_code_label=tkinter.Label(root, text='Source code can be found here. https://github.com/mark-IV-II/Project_hangman.git')

attempt_box=tkinter.Entry(root,width=5)
score_box=tkinter.Entry(root,width=5)   
output_box=tkinter.Entry(root,font='Calibri 16 bold',width=25,justify='center')
input_box=tkinter.Entry(root,width=5)
missed_box=tkinter.Entry(root,width=30)
quit_button=tkinter.Button(root,height=1,width=4,text='Quit',command=quit_game)
check_button=tkinter.Button(root,height=2,width=7,text='Check',command=check_ans)
reset_button=tkinter.Button(root,height=1,width=4,text='Reset',command=reset)

game_canvas.create_window(350,10,window=welcome_label)
game_canvas.create_window(100,75,window=attempt_label)
game_canvas.create_window(175,75,window=attempt_box)
game_canvas.create_window(700,75,window=score_label)
game_canvas.create_window(750,75,window=score_box)
game_canvas.create_window(400,125,window=output_label)
game_canvas.create_window(400,175,window=output_box)
game_canvas.create_window(200,250,window=input_label)
game_canvas.create_window(300,250,window=input_box)
game_canvas.create_window(200,300,window=missed_label)
game_canvas.create_window(350,300,window=missed_box)
game_canvas.create_window(50,375,window=quit_button)
game_canvas.create_window(375,375,window=check_button)
game_canvas.create_window(750,375,window=reset_button)
game_canvas.create_window(250,445,window=source_code_label)

params=parameters()
start()

root.mainloop()
