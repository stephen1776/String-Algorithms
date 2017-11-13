'''
Counting Point Mutations
Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
Return: The Hamming distance dH(s,t).
'''

import os

def hammingDistance(s,t):
    return sum(i != j for i, j in zip(s, t))

def main():
    filename = '../data/rosalind_hamm.txt'
    if os.path.isfile(filename) == True:
        with open(filename) as f:
            s, t = f.readlines()
            print(hammingDistance(s, t))


    else:#run sample data
        s = 'GAGCCTACTAACGGGAT'
        t = 'CATCGTAATGACGGCCT'
        print(hammingDistance(s,t))
        # sample output: 7


if __name__ == '__main__':
    main()
