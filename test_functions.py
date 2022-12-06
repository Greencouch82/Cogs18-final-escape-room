"""Tests for my functions."""

from functions import *
import mock
import builtins
import pytest

##
##

def test_time_convert():
    print('testing time convert function')
    assert callable(time_convert)
    assert time_convert(216066) == '60 hours, 1 minutes, 6 seconds'

    
    
def test_decrypt_caesar_2():
    print('testing decrypt 2')
    assert callable(decrypt_caesar_2)
    assert decrypt_caesar_2('EQFKPI',2) == 'CODING'
    
    

def test_ask_a_question():
    # specify after lambda what you want function to use as "input"
    with mock.patch.object(builtins, 'input', lambda _: 'B'):  #replace Hello with the input you would like to test

        # execute function and specify something that asserts True
        msg = ask_a_question('Testing ask_a_question', 'ABC')
        assert msg == 'B'  #replace Hello with what you expect to get back as output from your function
    
def test_password_solver():
    print('testing password solver function')
    assert callable(password_solver)

def test_trivia():
    print('testing trivia function')
    assert callable(trivia)
    
def test_basic_math():
    print('testing basic math function')
    assert callable(basic_math)

test_time_convert()

test_decrypt_caesar_2()

test_ask_a_question()
                 
test_password_solver()

test_trivia()

test_basic_math()