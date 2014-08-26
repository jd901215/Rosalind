__author__ = 'juanda'

"""
Problem

Recall the definition of the Fibonacci numbers from 'Rabbits and Recurrence Relations', which followed the recurrence
relation Fn = F(n-1) + F(n-2) and assumed that each pair of rabbits reaches maturity in one month and produces a single pair
of offspring (one male, one female) each subsequent month.

Our aim is to somehow modify this recurrence relation to achieve a dynamic programming solution in the case that all
rabbits die out after a fixed number of months.

Given: Positive integers n<=100 and m<=20.

Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.
"""
from os.path import dirname
from sys import argv

generations = [1, 1]  # Seed the sequence with the 1 pair, then in their reproductive month.

def mortal_fib(n, m):
    """
    :param n:
    :param m:
    :return:
    """
    count = 2
    while count < n:
        if count < m:
            # recurrence relation before rabbits start dying (simply mortal_fib seq Fn = Fn-2 + Fn-1)
            generations.append(generations[-2] + generations[-1])
        elif count == m or count == m+1:
             # Base cases for subtracting rabbit deaths (1 death in first 2 death gens)
            generations.append((generations[-2] + generations[-1]) - 1)  # Fn = Fn-2 + Fn-1 - 1
        else:
            # Our recurrence relation here is Fn-2 + Fn-1 - Fn-(m+1)
            generations.append((generations[-2] + generations[-1]) - (generations[-(m+1)]))
        count += 1
    return generations[-1]

def main():
    input_file = open(dirname(__file__)+argv[1]).read().split()
    print mortal_fib(int(input_file[0]), int(input_file[1]))

if __name__ == '__main__':
    main()
