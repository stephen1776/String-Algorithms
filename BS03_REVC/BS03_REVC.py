'''
Complementing a Strand of DNA
Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement s^c of s.
'''
import os

def ReverseComplement(dna):
    dnaComplementDict = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}  # create dictionary
    complementDNA = [dnaComplementDict[i] for i in dna]  # complement the dna
    return complementDNA[::-1]  # reverse the complement


def main():
    filename = '../data/rosalind_revc.txt'
    if os.path.isfile(filename) == True:
        with open(filename) as f:
            dna = f.read().strip()
            print(''.join(ReverseComplement(dna)))
    else:
        dna = 'AAAACCCGGT'
        print(''.join(ReverseComplement(dna)))
        # sample output = ACCGGGTTTT

if __name__ == '__main__':
    main()
