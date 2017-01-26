from unittest import TestCase

from chapter_17.letters_and_numbers import letters_numbers, letters_numbers_brute_force


class TestLettersNumbers(TestCase):
    def test(self):
        a = "abs12367as6723sdf672476fs765huj24njjh3j3hb2h"
        assert letters_numbers_brute_force(a) == letters_numbers(a)
