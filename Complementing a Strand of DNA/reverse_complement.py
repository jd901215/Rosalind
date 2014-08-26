__author__ = 'juanda'

import sys
from os.path import dirname

def main():

    output = ''
    complements = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}

    text = open(sys.argv[1])
    for line in text:
        for letter in line:
            if letter.isalpha():
                output += complements[letter]

    print output[::-1]

if __name__ == '__main__':

    main()