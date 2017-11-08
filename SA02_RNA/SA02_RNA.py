'''
Transcribing DNA into RNA
Given: A DNA string t having length at most 1000 nt.

Return: The transcribed RNA string of t.
'''
import os

def TranscribingDNAtoRNA(dna):
    rna = dna.replace('T', 'U')
    return rna



if __name__ == '__main__':
    filename = '../data/rosalind_rna.txt'
    if os.path.isfile('../data/rosalind_rna.txt') == True:
        with open(filename) as f:
            dna = f.read().strip()
            print(TranscribingDNAtoRNA(dna).replace(' ', ''))
    else:
        dna = 'GATGGAACTTGACTACGTAAATT'
        print(TranscribingDNAtoRNA(dna).replace(' ', ''))
        # sample output = GAUGGAACUUGACUACGUAAAUU