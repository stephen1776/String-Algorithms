'''
Mendel's First Law
Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms:
k individuals are homozygous dominant for a factor,
m are heterozygous, and
n are homozygous recessive.

Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant
allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.
___
'''
import os

def mendel_first(k, m, n):
    '''
    Find the four cases that result in an organism without a dominant allele, then subtract that from 1 to get
    the probability of an individuL that displays the dominant trait.
    '''

    population = float(k + m + n)
    prob_1 = (n / population) * (n - 1) / (population - 1) * 1.0
    prob_2 = (m / population) * (m - 1) / (population - 1) * 1 / 4
    prob_3 = (m / population) * n / (population - 1) * 1 / 2
    prob_4 = (n / population) * m / (population - 1) * 1 / 2

    prob = 1 - (prob_1 + prob_2 + prob_3 + prob_4)

    return prob


def main():
    filename = '../data/rosalind_iprb.txt'
    if os.path.isfile(filename) == True:
        with open(filename) as f:
            k, m, n = [int(x) for x in f.read().split()]
            print('%.6f' % mendel_first(k,m,n))


    else:#run sample data
        k, m, n = 2, 2, 2
        print('%.5f' % mendel_first(k,m,n))
        # sample output: 0.78333


if __name__ == '__main__':
    main()


