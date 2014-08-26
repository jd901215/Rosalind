__author__ = 'juanda'

'''

The basic rule is the same: it takes 1 month to for a pair to mature

Therefore at:

Month 0: 1 pair exists (young)

Month 1: 1 pair exists (adult)

Month 2: 1 pair exists (adult) + k pairs exist (young) = 1 + k total

Month 3: 1 + k pairs exist (adult) + k pairs exist (young) = 1 + 2k total

Month 4: 1 + 2k pairs exist (adult) + k (1 + k) pairs exist (young) = 1 + k(3 + k) total

Month 5: 1 + 3k + k^2 pairs exist (adult) + k (1 + 2k) pairs exist (young) = 1 + k(4 + 3k) total

'''

import sys
from os.path import dirname

def main():

    input_file = open(dirname(__file__)+sys.argv[1]).read()
    n, k = map(int,input_file.strip().split())
    rabbits = fibonacci(n-1,k)
    print rabbits

def fibonacci(n,k):
    """
    Test:

    >>> fibonacci(4, 3)
    19
    >>> fibonacci(3, 3)
    7
    """

    if n is 0 or n is 1: return 1
    else: return (fibonacci(n-1,k) + k*fibonacci(n-2,k))


if __name__ == '__main__':

    import doctest
    doctest.testmod()

    main()