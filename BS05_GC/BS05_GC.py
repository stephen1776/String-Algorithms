'''
Computing GC Content
Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
Return: The ID of the string having the highest GC-content, followed by the GC-content of that string.
'''
import os; from BS_UTILS import parseFasta

def gcContent(fastas):
    max_gc = 0
    max_seq_id = ''

    for seq_id, seq in fastas.items():
        gc_content = float( ((seq.count('G') + seq.count('C')) / len(seq) ) * 100)
        if gc_content > max_gc:
            max_gc = gc_content
            max_seq_id = seq_id

    return (max_seq_id, max_gc)


def main():
    filename = '../data/rosalind_gc.txt'
    if os.path.isfile(filename) == True:
        fastas = parseFasta(filename, no_id=False)
        max_seq_id, max_gc = gcContent(fastas)

        print(max_seq_id, '\n', '%.5f' % max_gc, sep='')

    else:#run sample data
        fastas = parseFasta(file='../data/gcContent.txt', no_id=False)
        max_seq_id, max_gc = gcContent(fastas)
        print(max_seq_id, '\n', '%.4f' % max_gc, sep='')
        # sample output:
        # Rosalind_0808
        # 60.919540



if __name__ == '__main__':
    main()

