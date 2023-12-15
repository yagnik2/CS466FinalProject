import needlemenwunsch.py

def forwards(x, y, simMatrix, gapPenalty, alphEnum):
    len_1, len_2 = len(x), len(y)
    curr = []
    for i in range(len_1+1):
        curr.append([0]*(len_2+1))
    for j in range(len_2+1):
        curr[0][j] = gapPenalty*j
    for i in range(1, len_1+1):
        curr[i][0] = curr[i-1][0] + gapPenalty
        for j in range(1, len_2+1):
            curr[i][j] = max(curr[i-1][j-1] + simMatrix[alphEnum[x[i-1]]][alphEnum[y[j-1]]],
                            curr[i-1][j] + gapPenalty,
                            curr[i][j-1] + gapPenalty)
        # Now clear row from memory.
        curr[i-1] = []
    return curr[len_1]

def backwards(x, y, simMatrix, gapPenalty, alphEnum):
    # This is the backwards subroutine.
    len_1, len_2 = len(x), len(y)
    curr = []
    for i in range(len_1+1):
        curr.append([0]*(len_2+1))
    for j in range(len_2+1):
        curr[0][j] = gapPenalty*j
    for i in range(1, len_1+1):
        curr[i][0] = curr[i-1][0] + gapPenalty
        for j in range(1, len_2+1):
            curr[i][j] = max(curr[i-1][j-1] + simMatrix[alphEnum[x[len_1-i]]][alphEnum[y[len_2-j]]],
                            curr[i-1][j] + gapPenalty,
                            curr[i][j-1] + gapPenalty)
        # Now clear row from memory.
        curr[i-1] = []
    return curr[len_1]


def hirschberg(x, y, simMatrix, gapPenalty, alphEnum):
    len_1, len_2= len(x), len(y)
    F = forwards(x[:len_1/2], y, simMatrix, gapPenalty, alphEnum) 
    B = backwards(x[len_1/2:], y, simMatrix, gapPenalty, alphEnum)
    split = [F[j] + B[len_2-j] for j in range(len_2+1)]
    diff = split.index(max(split))
    F, B, split = [], [], []
    left_call = hirschberg(x[:len_1/2], y[:diff], simMatrix, gapPenalty, alphEnum)
    right_call = hirschberg(x[len_1/2:], y[diff:], simMatrix, gapPenalty, alphEnum)
    return [left_call[r] + right_call[r] for r in range(3)]