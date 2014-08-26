__author__ = 'juanda'

from doctest import testmod

def parse_fasta(fasta_string):
    """
    :param fasta_string: string with genetic srings in FASTA format
    :return: A dictionary with key> FASTA ID value> Genetic String

    :testmod
    >>> text = open('test.txt').read()
    >>> parse_fasta(text)
    {'Rosalind_6404': 'CCTGCG', 'Rosalind_5959': 'CCATC': 'Rosalind_0808': 'CCACC'}
    """

    genetic_strings = {}
    record_id = None
    for line in [ l.strip() for l in fasta_string.splitlines()]:

        if line[0] is '>':
            record_id = line[1:]
            genetic_strings[record_id] = ''
        else:
            genetic_strings[record_id] += line


    return genetic_strings

if __name__ == "__main__":
    testmod()