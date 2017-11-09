'''
Rabbits and Recurrence Relations
Given: Positive integers n≤40 and k≤5.

Return: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each
generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).
'''
import os

def fib(n,k):
    a, b = 0, 1
    for i in range(1, n):
        a, b = b, k * a + b
    return b

if __name__ == '__main__':
    filename = '../data/rosalind_fib.txt'
    if os.path.isfile('../data/rosalind_fib.txt') == True:
        with open(filename) as f:
            line = f.read().split()
            n = int(line[0])
            k = int(line[1])
            print(fib(n,k))
    else:
        n = 5
        k = 3
        #print(fib(n,k))
        # sample output = 19