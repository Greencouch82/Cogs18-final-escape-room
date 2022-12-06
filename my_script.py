"""Script to run the main part of my project. It imports the functions and executes the gameplay."""

import sys
sys.path.append('../')

# Imports
from functions import *

import random
import time  

# main program
player_name = ""

while player_name == "": # repeats the question until there is an answer
    player_name = input('What is your name? ')
        
print('Welcome' + ' '+ player_name + '!')
start_time = time.time() # starts the stopwatch

remaining_tasks = ['A', 'B', 'C'] # list of tasks that still need to be completed - will be mutated as the player progresses

print('You are a spy, trapped in an enemy compound. Time to steal info and escape! Good luck!')
print()
print('Spelling and capitalization matter, so be careful.')
print()

while len(remaining_tasks) != 0: # main game loop that continues until all tasks are completed (in whatever order the player chooses)
    
    back_story = """You look around the room. You see """ # sets up the sentence

    if 'A' in remaining_tasks: # adds A to the sentence if it hasn't been completed yet
        back_story = back_story + 'a computer (A) '
    if 'B' in remaining_tasks: # adds B to the sentence if it hasn't been completed yet
        back_story = back_story + 'a file folder (B) '
    if 'C' in remaining_tasks: # adds C to the sentence if it hasn't been completed yet
        back_story = back_story + 'a calculator (C)'

    back_story = back_story + '. Which one do you want to examine?' # finishes the sentence

    answer = ask_a_question(back_story,remaining_tasks) # lets the player choose which task to do 

    if answer == 'A': # if player chose A, this runs the password_solver function until the player gets it right
        password_solver()
        print('Good job!')
    
    if answer == 'B': # if player chose B, this runs the trivia function until the player gets it right
        trivia()
        print('You did it!')
    
    if answer == 'C': # if player chose C, this runs the basic_math function until the player gets it right
        basic_math()
        print('Nice one!')
        
    remaining_tasks.remove(answer) # removes the completed task from remaining tasks list

# end of main while loop, i.e. the following will happen when all 3 tasks are completed
print()
print('Congratulations! You have successfully exfiltrated enemy headquarters and stolen valuable information for your own organization.')

end_time = time.time() # stops the stopwatch
print('It took you', time_convert(end_time - start_time), 'to escape.') # informs the player how long they took 
print()
print('Good luck on future endeavors, ' + player_name + '!')
print('GAME OVER')