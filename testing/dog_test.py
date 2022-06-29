#!/usr/bin/env python

from lib.dog import Dog

class TestDog:
    '''Dog in dog.py'''

    def test_is_class(self):
        '''is a class with the name "Dog"'''
        fido = Dog("Fido")
        assert(type(fido) == Dog)

class TestInit:
    '''Dog.__init__ in dog.py'''

    def test_saves_self_name(self):
        '''takes a name as an argument and saves it to self.name'''
        fido = Dog("Fido")
        assert(fido.name == "Fido")

    def test_saves_self_breed(self):
        '''takes a breed as an argument and saves it to self.breed'''
        fido = Dog("Fido", "Dalmatian")
        assert(fido.breed == "Dalmatian")

    def test_default_breed(self):
        '''sets self.breed = "Mutt" when no breed specified'''
        fido = Dog("Fido")
        assert(fido.breed == "Mutt")
