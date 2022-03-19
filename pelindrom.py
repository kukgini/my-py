def solution(n,m):
    answer = 0
    for i in range(n,m+1):
        s = str(i)
        l = len(s)
        h = int(l / 2)
        if l == 1:
            answer = answer + 1
        else:
            b = True
            for j in range(0,h):
                x = s[j]
                y = s[l-j-1]
                r = x == y
                b = b and r
            if b == True:
                answer = answer + 1
    return answer