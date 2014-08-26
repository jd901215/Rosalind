__author__ = 'juanda'
'''
A matrix is a rectangular table of values divided into rows and columns. An mxn matrix has m rows and n columns.
Given a matrix A, we write Ai,j to indicate the value found at the intersection of row i and column j.

Say that we have a collection of DNA strings, all having the same length n. Their profile matrix is a 4xn matrix P in
which P1,j represents the number of times that 'A' occurs in the jth position of one of the strings, P2,j represents
the number of times that C occurs in the jth position, and so on (see below).

A consensus string c is a string of length n formed from our collection by taking the most common symbol at each
position; the jth symbol of c therefore corresponds to the symbol having the maximum value in the j-th column of the
profile matrix. Of course, there may be more than one most common symbol, leading to multiple possible consensus
strings.

DNA Strings	    A T C C A G C T
	            G G G C A A C T
	            A T G G A T C T
 	            A A G C A A C C
	            T T G G A A C T
	            A T G C C A T T
	            A T G G C A C T


Profile	        A   5 1 0 0 5 5 0 0
	            C   0 0 1 4 2 0 6 1
	            G   1 1 6 3 0 1 0 0
	            T   1 5 0 0 0 1 1 6

Consensus	        A T G C A A C T

Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then
you may return any one of them.)
'''

import sys

sys.path.append("/home/juanda/PycharmProjects/Rosalind")

import numpy as np
from sys import argv
from utils.utilities import parse_fasta
from os.path import dirname


def get_profile_consensus(fasta_string):
    """
    :param fasta_string: An unformatted fasta string
    :return:  A matrix encoding the number of times that each symbol of an alphabet occurs in each position from a
                collection of strings. (profile_matrix) and a consensus string
    """
    a_profile = 'A:'
    c_profile = 'C:'
    g_profile = 'G:'
    t_profile = 'T:'

    index_dict = { 0:'A', 1:'C', 2:'G', 3:'T'}

    formated_fasta = parse_fasta(fasta_string)
    array_argument = []
    consensus = ''

    for name, genetic_string in formated_fasta.items():
        array_argument.append(list(genetic_string))

    array_size = len(genetic_string)
    array = np.array(array_argument)

    for index in range(array_size):
        a_profile += ' ' + str(list(array[:,index]).count('A'))
        c_profile += ' ' + str(list(array[:,index]).count('C'))
        g_profile += ' ' + str(list(array[:,index]).count('G'))
        t_profile += ' ' + str(list(array[:,index]).count('T'))

    printable_profile_matrix = a_profile + '\n' + c_profile + '\n' + g_profile + '\n' + t_profile

    matrix = np.matrix(a_profile[2:]+'; ' + c_profile[2:] + '; ' + g_profile[2:] + '; ' + t_profile[2:])

    for index in range(array_size):
        highest = np.nanargmax(matrix[:,index])
        consensus += index_dict[highest]

    return consensus, printable_profile_matrix


def main():
    input_file = open(dirname(__file__)+argv[1]).read()
    consensus, matrix =  get_profile_consensus(input_file)
    answer = open('answer.txt','w')
    answer.write(consensus)
    answer.write('\n')
    answer.write(matrix)

if __name__ == "__main__":
    main()