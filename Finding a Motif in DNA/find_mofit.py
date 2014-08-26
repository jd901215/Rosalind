__author__ = 'juanda'

'''
Given two strings s and t, t is a substring of s if t is contained as a contiguous collection of symbols in s
(as a result, t must be no longer than s).

The position of a symbol in a string is the total number of symbols found to its left, including itself
(e.g., the positions of all occurrences of 'U' in "AUGCUUCAGAAAGGUCUUACG" are 2, 5, 6, 15, 17, and 18). The symbol at
position i of s is denoted by s[i].

A substring of s can be represented as s[j:k], where j and k represent the starting and ending positions of the
substring in s; for example, if s = "AUGCUUCAGAAAGGUCUUACG", then s[2:5] = "UGCU".

The location of a substring s[j:k] is its beginning position j; note that t will have multiple locations in s if it
occurs more than once as a substring of s (see the Sample below).

Given: Two DNA strings s and t (each of length at most 1 kbp).

Return: All locations of t as a substring of s.

'''
from os.path import dirname
from regex import finditer
from sys import argv

def main():
    input_file = open(dirname(__file__)+argv[1]).read()
    elements = input_file.splitlines()
    r =  find_mofit(elements[0], elements[1])
    answer = open('answer.txt','w')
    answer.write(r)

def find_mofit(s, t):
    """
    :return: All locations of t as a substring of s.
    :param: s, t Two DNA strings
    """
    matches = finditer(t, s, overlapped=True)
    ans = [ str(element.start()+1) for element in matches]
    return ' '.join(ans)

if __name__ == '__main__':
    main()