'''
Consensus and Profile: Finding a Most Likely Common Ancestor
Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

Return: A consensus string and profile matrix for the collection.
'''
from BS_UTILS import parseFasta

def dnaToProfile(dna):
    #Make a profile matrix from the list of DNA sequences
    motif_length = len(min(dna))
    prof_matrix = [[0 for i in range(4)] for j in range(motif_length)]

    prof_dict = {'A':0, 'C':1, 'G':2, 'T':3}
    for i in range(motif_length):
        for seq in dna:
            s = seq[i]
            if s in prof_dict:
                prof_matrix[i][prof_dict[s]] += 1

    return prof_matrix

def profileToConsensus(profile):
    # Find the consensus motif from profile matrix
    consensus = ''
    out = ['A', 'C', 'G', 'T']
    for i in range(len(profile)):
        m = profile[i].index(max(profile[i]))
        consensus += out[m]

    return consensus


def profileMatrix(profile):
    # Use a generator to format the profile matrix
    alphabet = ['A', 'C', 'G', 'T']

    for i in range(4):
        line = alphabet[i] + ': '
        for j in range(len(profile)):
            line += str(profile[j][i]) + ' '

        yield line


def main():
    filename = '../data/rosalind_cons.txt'
    motif = parseFasta(filename)
    profile = dnaToProfile(motif)
    consensus = profileToConsensus(profile)
    print(consensus)
    for line in profileMatrix(profile):
        print(line)

if __name__ == '__main__':
    main()
