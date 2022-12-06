# Functions for my project
import random

# define functions and procedures
def time_convert(sec):
    """
    Convert a time duration from seconds to a string in the readable format "X hours, Y minutes, Z seconds".
    (Adapted) reference for the time function: www.codespeedy.com/how-to-create-a-stopwatch-in-python/.
    
    Parameters:
    sec: An integer representing a time duration in seconds.

    Returns:
    A string representing the time duration in the format "X hours, Y minutes, Z seconds".

    Example:
    time_convert(3600) -> "1 hours, 0 minutes, 0 seconds"
    time_convert(60) -> "0 hours, 1 minutes, 0 seconds"
    time_convert(7261) -> "2 hours, 1 minutes, 1 seconds"
    """
    
    mins = sec // 60
    sec = int(sec % 60)
    hours = int(mins // 60)
    mins = int(mins % 60)
    
    return str(hours) + " hours, " + str(mins) + " minutes, " + str(sec) + " seconds"


def ask_a_question(question, answers, show_answers = True):
    """
    Ask a question and validate the user's answer.
    
    This function prints the question text (a string), asks for user input, and validates the user input.
    The function is easily adaptable to different situations, and can be used multiple times in a program.
    
    Parameters:
    - question: A string with the question the user has to answer
    - answers: A list or tuple of strings, representing the valid answers to the question.
    - show_answers: A boolean, indicating whether valid answers should be displayed if the user provides an invalid answer.
    
    Returns:
    - The user's answer, as a string.
    
    Example:
    ask_a_question('Choose A, B, or C.', 'ABC', show_answers = True) -> prints "Choose A, B, or C." 
    and asks for user input repeatedly until the answer is A, B, or C.
    """
    
    print()
    print(question)
    
    player_answer = input('input: ')
    while player_answer not in answers: # this part makes sure that user input exists and makes sense
        print('Sorry this is not the right answer. Try again.')
        if show_answers == True: # this part lets me decide if a wrong answer should display answer choices
            print('Valid answer chocies are: ', answers)
        player_answer = input('input: ')
    
    return player_answer


def decrypt_caesar_2(input_string, key = 2): 
    """
    Decrypt a string that was encrypted using a Caesar cipher with a shift of X (but could easily be adapted).
    Reference: Assignment 3

    Parameters:
    input_string: A string to be decrypted.
    key: An integer representing the shift used in the Caesar cipher. Defaults to 2.

    Returns:
    The decrypted string.

    Example:
    decrypt_caesar_2('EQFKPI', key = 2) -> 'CODING'
    """
    
    output_string = ''
    
    for char in input_string:
        output_string = output_string + chr(ord(char) - key)
    
    return output_string


def password_solver(): 
    """
    Prompt the user with ask_a_question to let the player solve the password through user input.

    Returns:
    None
    """
    
    print()
    
    encoded = 'EQFKPI'
    decoded = decrypt_caesar_2(encoded)
    
    ask_a_question('You have discovered a useful password! Unfortunately, it is encrypted, meaning you have to decrypt it before taking it back to your HQ! Luckily, you know that this is a simple "Caesar + 2" cipher, meaning the letter "A" was encrypted as "C" and "B" was encrypted as "D" and so on. Here is the keyword you found: ' + encoded, decoded, False)


def trivia(): 
    """
    This function chooses a random question from a given dictionary, 
    which could easily be expanded to make the game more complex, and has the user answer with the ask_a_question function.
    The dictionary contains questions and answers (about collection types in Python).
    
    Returns:
    None
    """
    
    print()
    print('You found an interesting file folder about Python. Luckily, you still remember a bit from your Cogs 18 class all those years ago.')
    
    trivia_dict = {'What do you call a collection in Python that uses square brackets, is mutable, and can be of mixed type?' : 'list', 
                   'What do you call a collection in Python that uses parentheses, is immutable, and can be of mixed type?' : 'tuple',
                   'What do you call a collection in Python that uses curly brackets, is mutable, and stores key-value pairs?' : 'dictionary'}
    
    selected_question = random.choice(list(trivia_dict))
    ask_a_question(selected_question, trivia_dict.get(selected_question), show_answers = False)
    


def basic_math(): 
    """
    This function uses the ask_a_question function to let the player solve a short math problem.
    
    Returns:
    None
    """
    
    print()
    print('There is a calculator on the desk. Wait! It is not a calculator! This is a secret keypad for a safe, and it requires you to do math in order to open the safe.')
    
    ask_a_question('The keypad has 3 keys - 1, 2, and 3. How many different 2-digit numbers are possible?', '9', show_answers = False)