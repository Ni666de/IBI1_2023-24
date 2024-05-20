def count_repeats(sequence, pattern):
    count = 0
    i = 0
    while i < len(sequence):
        if sequence[i:i+len(pattern)] == pattern:
            count += 1
            i += len(pattern)  
        else:
            i += 1
    return count

seq = 'ATGCAATCGGTGTGTCTGTTCTGAGAGGGCCTAA'
repeats = ['GTGTGT', 'GTCTGT']

for repeat in repeats:
    print(f"The repeat element '{repeat}' appears {count_repeats(seq, repeat)} times in the sequence.")
