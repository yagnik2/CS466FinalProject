def nw(A, B, simMatrix, gapPenalty, alphEnum):
    len_1, len_2 = len(A), len(B)
    curr = []
    for i in range(len_1+1):
        curr.append([0]*(len_2+1))
    for j in range(len_2+1):
        curr[0][j] = gapPenalty*j
    for i in range(len_1+1):
        curr[i][0] = gapPenalty*i
    for i in range(1, len_1+1):
        for j in range(1, len_2+1):
            curr[i][j] = max(curr[i-1][j-1] + simMatrix[alphEnum[A[i-1]]][alphEnum[B[j-1]]], curr[i][j-1] + gapPenalty, curr[i-1][j] + gapPenalty)
    alignment_1 = ""
    alignment_2 = ""
    i, j = len_1, len_2
    while i and j:
        score, score_diag, score_up, score_left = curr[i][j], curr[i-1][j-1], curr[i-1][j], curr[i][j-1]
        if score == score_diag + simMatrix[alphEnum[A[i-1]]][alphEnum[B[j-1]]]:
            alignment_1 = A[i-1] + alignment_1
            alignment_2 = B[j-1] + alignment_2
            i -= 1
            j -= 1
        elif score == score_up + gapPenalty:
            alignment_1 = A[i-1] + alignment_1
            alignment_2 = '-' + alignment_2
            i -= 1
        elif score == score_left + gapPenalty:
            alignment_1 = '-' + alignment_1
            alignment_2 = B[j-1] + alignment_2
            j -= 1
    while i:
        alignment_1 = A[i-1] + alignment_1
        alignment_2 = '-' + alignment_2
        i -= 1
    while j:
        alignment_1 = '-' + alignment_1
        alignment_2 = B[j-1] + alignment_2
        j -= 1
    return [alignment_1, alignment_2, curr[len_1][len_2]]