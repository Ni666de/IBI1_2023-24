import numpy as np

def read_sequence(path):
    with open(path, 'r') as file:
        return file.read().strip()

def load_blosum62():
    matrix = np.loadtxt('BLOSUM62.csv', delimiter=',')
    return matrix

def calculate_score(seq1, seq2, matrix):
    score = 0
    for a, b in zip(seq1, seq2):
        score += matrix[a, b]  # 根据BLOSUM62矩阵计算得分
    return score

def calculate_identity(seq1, seq2):
    identical = sum(a == b for a, b in zip(seq1, seq2))
    return (identical / len(seq1)) * 100

def main():
    seq1 = read_sequence('sequence1.txt')
    seq2 = read_sequence('sequence2.txt')
    
    blosum62 = load_blosum62()
    
    score = calculate_score(seq1, seq2, blosum62)
    identity = calculate_identity(seq1, seq2)
    
    print(f"Alignment score: {score}")
    print(f"Percentage of identical amino acids: {identity}%")

if __name__ == "__main__":
    main()
