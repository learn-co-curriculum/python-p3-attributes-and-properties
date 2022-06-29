#!/usr/bin/env python

from lib.dog import Dog

class TestDog:
    '''Dog in dog.py'''

    def test_is_class(self):
        '''is a class with the name "Dog"'''
        fido = Dog(name="Fido", breed="Corgi")
        assert(type(fido) == Dog)

    def test_name_zero_characters(self):
        fido = Dog(name="", breed="Corgi")
        