from Bio import SeqIO

def read_fasta(file_path):
    with open(file_path, "r") as file:
        return list(SeqIO.parse(file, "fasta"))

def extract_genes(sequences, keyword):
    duplicate_genes = []
    for seq in sequences:
        if keyword in seq.description:
            simplified_name = seq.description.split()[0]
            seq.id = simplified_name
            seq.name = simplified_name
            duplicate_genes.append(seq)
    return duplicate_genes

def write_fasta(sequences, output_file):
    with open(output_file, "w") as output_handle:
        SeqIO.write(sequences, output_handle, "fasta")

input_file = 'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
output_file = 'duplicate_genes.fa'

sequences = read_fasta(input_file)
duplicates = extract_genes(sequences, 'duplication')
write_fasta(duplicates, output_file)
