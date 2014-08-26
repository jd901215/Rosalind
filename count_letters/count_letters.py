__author__ = 'juanda'

import sys

def main():

    a = 0
    c = 0
    g = 0
    t = 0

    text = open(sys.argv[1])

    for line in text:
        a+=line.count("A")
        c+=line.count("C")
        g+=line.count("G")
        t+=line.count("T")

    print  str(a)+" "+str(c)+" "+str(g)+" "+str(t)

if __name__ == '__main__':
    main()