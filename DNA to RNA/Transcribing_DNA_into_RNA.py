__author__ = 'juanda'

import sys


def main():
    text = open(sys.argv[1])

    for line in text:
        print line.replace('T', 'U')

if __name__ == '__main__':
    main()