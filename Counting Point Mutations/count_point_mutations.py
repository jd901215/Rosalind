__author__ = 'juanda'

"""
Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t), is the number of
corresponding symbols that differ in s and t.

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t).
"""

from sys import argv
from doctest import testmod
from os.path import dirname
from itertools import *



def main():
    testmod()
    text = open(dirname(__file__)+argv[1]).read()
    genetic_strings = text.splitlines()
    print cpm(genetic_strings)

def cpm(genetic_strings):
    '''
    :param genetic_strings: list with the two genetic strings to compare
    :return: hamming_distance: The minimum number of symbol substitutions required to transform one string
    into the other.
    :testmod
    >>> cpm(['GAGCCTACTAACGGGAT', 'CATCGTAATGACGGCCT'])
    7
    '''

    zip_strings = izip_longest(genetic_strings[0], genetic_strings[1], fillvalue='-')
    hamming_distance = 0

    for element in zip_strings:
        if element[0] != element[1]:
            hamming_distance += 1

    return hamming_distance

if __name__ == '__main__':
    main()


