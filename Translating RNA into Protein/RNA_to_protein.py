__author__ = 'juanda'

'''
The 20 commonly occurring amino acids are abbreviated by using 20 letters from the English alphabet
(all letters except for B, J, O, U, X, and Z). Protein strings are constructed from these 20 symbols.
Henceforth, the term genetic string will incorporate protein strings along with DNA strings and RNA strings.

The RNA codon table dictates the details regarding the encoding of specific codons into the amino acid alphabet.

Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).

Return: The protein string encoded by s.
'''

import sys
sys.path.append("/home/juanda/PycharmProjects/Rosalind")

from utils import utilities
from re import findall
from sys import argv
from os.path import dirname



def rna_encoder(genetic_string):
    """
    :param genetic_string: A RNA string corresponding to a strand of mRNA
    :return protein_string:  The protein string encoded by genetic_string
    """

    protein_string = ''

    for codon in findall('...', genetic_string):
        if utilities.RNA_codon_table[codon] == 'STOP':
            protein_string += '\n'
            return protein_string
        elif utilities.RNA_codon_table.has_key(codon):
            protein_string += utilities.RNA_codon_table[codon]

    return protein_string


def main():
    input_file = open(dirname(__file__)+argv[1]).read()
    r =  rna_encoder(input_file)
    answer = open('answer.txt','w')
    answer.write(r)

if __name__ == '__main__':
    main()