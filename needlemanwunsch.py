def needlemanwunsh(A, B, scores, alphtoint, gaps=-1):
    A_output = ""
    B_output = ""

    curr = []
    for i in range(len(A)+1):
        curr.append([0]*(len(B)+1))

    for i in range(len(B)+1):
        curr[0][i] = gaps*i

    for i in range(len(A)+1):
        curr[i][0] = gaps*i

    for i in range(1, len(A)+1):
        for j in range(1, len(B)+1):
            curr[i][j] = max(curr[i][j-1]+gaps, curr[i-1][j]+gaps,curr[i-1][j-1]+scores[alphtoint[A[i-1]]][alphtoint[B[j-1]]])
    
    i, j = len(A), len(B)
    while i>0 and j>0:  
        if curr[i][j] == curr[i-1][j]+gaps:
            A_output = A[i-1]+A_output
            B_output = '-'+B_output
            i -= 1

        elif curr[i][j] == curr[i][j-1]+gaps:
            A_output = '-'+A_output
            B_output = B[j-1]+B_output
            j -= 1

        elif curr[i][j] == curr[i-1][j-1]+scores[alphtoint[A[i-1]]][alphtoint[B[j-1]]]:
            A_output = A[i-1]+A_output
            B_output = B[j-1]+B_output
            i -= 1
            j -= 1

    while i>0:
        A_output = A[i-1]+A_output
        B_output = '-'+B_output
        i -= 1

    while j>0:
        A_output = '-'+A_output
        B_output = B[j-1]+B_output
        j -= 1
        
    return [A_output, B_output, curr[len(A)][len(B)]]
