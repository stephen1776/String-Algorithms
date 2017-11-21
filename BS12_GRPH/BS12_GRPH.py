'''
Overlap Graphs

Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.
Return: The adjacency list corresponding to O3. You may return edges in any order.
'''
from BS_UTILS import parseFasta

def overlapGraphs(dna):
    for h1, s1 in dna.items():
        suffix = s1[-3:]
        for h2, s2 in dna.items():
            prefix = s2[:3]
            if s1 != s2:
                if suffix == prefix:
                    yield (' '.join([h1, h2]))



def main():
    filename = '../data/rosalind_grph2.txt'
    dna = parseFasta(filename, no_id=False)
    for line in overlapGraphs(dna):
        print(line)




if __name__ == '__main__':
    main()
