#!/usr/bin/env python3

class MyString:
    def __init__(self, value=''):
        self._value = ''
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        if not isinstance(val, str):
            print("The value must be a string.")
        else:
            self._value = val

    def is_sentence(self):
        return self._value.endswith('.')

    def is_question(self):
        return self._value.endswith('?')

    def is_exclamation(self):
        return self._value.endswith('!')

    def count_sentences(self):
        import re
        # Split on sentence-ending punctuation marks: ., !, ?
        # Use regex to split and filter out empty strings
        sentences = re.split(r'[.!?]+', self._value)
        # Filter out empty strings and strings with only whitespace
        sentences = [s for s in sentences if s.strip()]
        return len(sentences)
