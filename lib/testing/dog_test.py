#!/usr/bin/env python3

from dog import Dog

import io
import sys

class TestDog:
    '''Dog in dog.py'''

    def test_is_class(self):
        '''is a class with the name "Dog".'''
        fido = Dog()
        assert(type(fido) == Dog)
        
    def test_name_not_empty(self):
        '''prints "Name must be string between 1 and 25 characters." if empty string.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        Dog(name="")
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "Name must be string between 1 and 25 characters.\n")

    def test_name_string(self):
        '''prints "Name must be string between 1 and 25 characters." if not string.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        Dog(name=123)
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "Name must be string between 1 and 25 characters.\n")

    def test_name_under_25(self):
        '''prints "Name must be string between 1 and 25 characters." if string over 25 characters.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        Dog(name="What do dogs do on their day off? Can't lie around - that's their job.")
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "Name must be string between 1 and 25 characters.\n")

    def test_valid_name(self):
        '''saves name if string between 1 and 25 characters.'''
        fido = Dog(name="Fido")
        assert(fido.name == "Fido")

    def test_breed_not_in_list(self):
        '''prints "Breed must be in list of approved breeds." if not in breed list.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        Dog(breed="Human")
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "Breed must be in list of approved breeds.\n")

    def test_breed_in_list(self):
        '''saves breed if in breed list.'''
        fido = Dog(breed="Pug")
        assert(fido.breed == "Pug")
