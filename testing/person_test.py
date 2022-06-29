#!/usr/bin/env python

from lib.person import Person

class TestPerson:
    '''Person in person.py'''

    def test_is_class(self):
        '''is a class with the name "Person"'''
        guido = Person("Guido")
        assert(type(guido) == Person)

class TestInit:
    '''Person.__init__ in person.py'''

    def test_saves_self_name(self):
        '''takes a name as an argument and saves it to self.name'''
        guido = Person("Guido")
        assert(guido.name == "Guido")
