'''
Counting DNA Nucleotides
Given: A DNA string s of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and
'T' occur in s.
'''
import os

def CountingDNANucleotides(dna):
    result = []
    for i in 'ACGT':
        result.append(dna.count(i))
    return result



if __name__ == '__main__':
    filename = 'data/rosalind_dna.txt'
    if os.path.isfile('data/rosalind_dna.txt') == True:
        with open(filename) as f:
            dna = f.read().strip()
            print(*CountingDNANucleotides(dna))
    else:
        dna = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
        print(*CountingDNANucleotides(dna))
        # sample output = 20 12 17 21
