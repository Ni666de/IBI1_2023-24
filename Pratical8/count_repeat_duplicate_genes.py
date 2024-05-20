from Bio import SeqIO

def count_repeats(sequence, pattern):
    return sequence.count(pattern)

def extract_genes_with_repeats(sequences, pattern):
    genes_with_repeats = []
    for seq in sequences:
        if 'duplication' in seq.description and count_repeats(str(seq.seq), pattern) > 0:
            gene_name = seq.description.split()[0]
            repeat_count = count_repeats(str(seq.seq), pattern)
            genes_with_repeats.append((gene_name, repeat_count))
    return genes_with_repeats

def write_fasta(genes_with_repeats, output_filename):
    with open(output_filename, "w") as output_handle:
        for gene_name, repeat_count in genes_with_repeats:
            description = f"{gene_name}_repeat_{repeat_count}"
            seq_record = SeqIO.SeqRecord(
                SeqIO.Seq(str(sequences[gene_name].seq)), 
                id=gene_name,
                name=description,
                description=description
            )
            SeqIO.write(seq_record, output_handle, "fasta")

if __name__ == "__main__":
    input_file = 'duplicate_genes.fa' 
    sequences = read_fasta(input_file)
    
    pattern = input("Enter the repetitive sequence ('GTGTGT' or 'GTCTGT'): ")
  
    genes_with_repeats = extract_genes_with_repeats(sequences, pattern)
    
    output_filename = f"{pattern}_duplicate_genes.fa"
    
    write_fasta(genes_with_repeats, output_filename)
    print(f"Output written to {output_filename}")
