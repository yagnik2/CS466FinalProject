from needlemanwunsch import needlemanwunsh

def hirschberg(A, B, scores, alphtoint, gaps = -1):
    if len(A)>1 and len(B)>1:
        A1 = A[:(len(A)//2)]

        curr = []
        for i in range(len(A1)+1):
            curr.append([0]*(len(B)+1))
        for i in range(len(B)+1):
            curr[0][i] = gaps*i
        for i in range(1, len(A1)+1):
            curr[i][0] = curr[i-1][0]+gaps
            for j in range(1, len(B)+1):
                curr[i][j] = max(curr[i-1][j] + gaps, curr[i][j-1]+gaps,curr[i-1][j-1]+scores[alphtoint[A1[i-1]]][alphtoint[B[j-1]]])
            curr[i-1] = []

        pref = curr[len(A1)]

        A2 = A[(len(A)//2):]

        curr = []
        for i in range(len(A2)+1):
            curr.append([0]*(len(B)+1))
        for i in range(len(B)+1):
            curr[0][i] = gaps*i
        for i in range(1, len(A2)+1):
            curr[i][0] = curr[i-1][0]+gaps
            for j in range(1, len(B)+1):
                curr[i][j] = max(curr[i-1][j]+gaps,curr[i][j-1]+gaps,curr[i-1][j-1]+scores[alphtoint[A2[len(A2)-i]]][alphtoint[B[len(B)-j]]])
            curr[i-1] = []
        suff =  curr[len(A2)]

        midpts = []

        for i in range(len(B)+1):
            midpts.append(pref[i] + suff[len(B)-i])
        
        diff = midpts.index(max(midpts))

        topleft = hirschberg(A[:len(A)//2],B[:diff],scores,alphtoint,gaps)
        btmright = hirschberg(A[len(A)//2:],B[diff:],scores,alphtoint,gaps)

        output = []
        for i in range(3):
            output.append(topleft[i] + btmright[i])
        return output
    else:
        return needlemanwunsh(A,B,scores,alphtoint,gaps)