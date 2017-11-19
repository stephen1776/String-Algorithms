'''
Finding a Motif in DNA
Given: Two DNA strings s and t (each of length at most 1 kbp).

Return: All locations of t as a substring of s.
'''


def findingMotifs(s,t):
    inds = []
    for i in range(len(s)):
        if s.startswith(t, i):
            inds.append(i+1)
    return inds

def main():
    filename = '../data/rosalind_subs.txt'
    with open(filename) as f:
        s, t = f.read().strip().split('\n')
        print(*findingMotifs(s,t))


if __name__ == '__main__':
    main()
