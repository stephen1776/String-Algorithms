'''
Translating RNA into Protein
Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).
Return: The protein string encoded by s.
'''
import os; from BS_UTILS import codonTable

def translateRNA(rna):
    ct = codonTable('rna')
    protein = ''

    for i in range(0, len(rna), 3):
        rna_codon = rna[i:i + 3]
        amino_acid = ct.get(rna_codon, '$')
        if amino_acid != '$':
            protein += amino_acid
        else:
            break

    return protein


def main():
    filename = '../data/rosalind_prot.txt'
    if os.path.isfile(filename) == True:
        with open(filename) as f:
            rna = f.read().strip()
            print(translateRNA(rna))


    else:  # run sample data
        rna = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'
        print(translateRNA(rna))
        # sample output: MAMAPRTEINSTRING

if __name__ == '__main__':
    main()