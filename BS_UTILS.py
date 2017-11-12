
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
    else: # If no_id is set to False, return a dictionary of sequences with associated sequence id.
        return dict(zip(seq_ids, seqs))
