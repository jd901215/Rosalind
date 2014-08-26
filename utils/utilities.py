__author__ = 'juanda'

from doctest import testmod

RNA_codon_table = {"UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
                   "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
                   "UAU": "Y", "UAC": "Y", "UAA": "STOP", "UAG": "STOP",
                   "UGU": "C", "UGC": "C", "UGA": "STOP", "UGG": "W",
                   "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
                   "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
                   "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
                   "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
                   "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
                   "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
                   "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
                   "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
                   "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
                   "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
                   "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
                   "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G", }


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
    for line in [l.strip() for l in fasta_string.splitlines()]:

        if line[0] is '>':
            record_id = line[1:]
            genetic_strings[record_id] = ''
        else:
            genetic_strings[record_id] += line

    return genetic_strings


if __name__ == "__main__":
    testmod()