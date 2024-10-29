#!/usr/bin/env python3

from person import Person
import io
import sys

class TestPerson:
    '''Tests for the Person class in person.py'''

    @staticmethod
    def capture_output(func, *args, **kwargs):
        """Helper method to capture stdout output."""
        captured_out = io.StringIO()
        sys.stdout = captured_out
        func(*args, **kwargs)
        sys.stdout = sys.__stdout__
        return captured_out.getvalue()

    def test_is_class(self):
        '''Check if the instance is of type Person.'''
        guido = Person(name='Guido', job='Sales')
        assert isinstance(guido, Person)

    def test_name_not_empty(self):
        '''Should print an error if the name is an empty string.'''
        output = self.capture_output(Person, name="", job="Sales")
        assert output == "Name must be string between 1 and 25 characters.\n"

    def test_name_string(self):
        '''Should print an error if the name is not a string.'''
        output = self.capture_output(Person, name=123, job='Sales')
        assert output == "Name must be string between 1 and 25 characters.\n"

    def test_name_length(self):
        '''Should print an error if the name is longer than 25 characters.'''
        long_name = "What do Persons do on their day off? Can't lie around - that's their job."
        output = self.capture_output(Person, name=long_name, job='Sales')
        assert output == "Name must be string between 1 and 25 characters.\n"

    def test_valid_name(self):
        '''Should save the name if it's a valid string.'''
        guido = Person(name="Guido", job="Sales")
        assert guido.get_name() == "Guido"

    def test_valid_name_title_case(self):
        '''Should convert the name to title case if valid.'''
        guido = Person(name="guido van rossum", job="Sales")
        assert guido.get_name() == "Guido Van Rossum"

    def test_job_not_in_list(self):
        '''Should print an error if the job is not in the approved list.'''
        output = self.capture_output(Person, name="Guido", job="Benevolent dictator for life")
        assert output == "Job must be in list of approved jobs.\n"

    def test_job_in_list(self):
        '''Should save the job if it is in the approved list.'''
        guido = Person(name="Guido", job="ITC")
        assert guido.get_job() == "ITC"
