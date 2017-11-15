
def parseFasta(file, no_id=True):

    seq_ids = []
    seqs = []

    with open(file, 'r') as f: # Read in a Fasta file.
        for line in f.readlines():
            if line.startswith('>'):
                seq_ids.append(line[1:].strip())
                seqs.append('')
            else:
                seqs[-1] += line.strip()

    if no_id == True: # If no_id is set to True, return a list of sequences only.
        if len(seqs) > 1:
            return seqs
        else:
            return seqs[0]
    else: # If no_id is set to False, return sequences with associated sequence id.
        return dict(zip(seq_ids, seqs))


def codonTable(seq_type='rna'):
    if seq_type == 'rna':
        bases = ['U', 'C', 'A', 'G']
    else:
        bases = ['T', 'C', 'A', 'G']
    # See Codon table http://rosalind.info/glossary/rna-codon-table/
    codons = [a + b + c for a in bases for b in bases for c in bases]
    amino_acids = 'FFLLSSSSYY$$CC$WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG' # $ = stop
    # Will need to call by 3's
    codon_table = dict(zip(codons, amino_acids))

    return codon_table # Return codons and corresponding amino acids