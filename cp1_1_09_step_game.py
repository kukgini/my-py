def func(record):
    if record == 0:
        return 1
    elif record == 1:
        return 2
    return 0

def solution(a,b):
    cnt = 0 # A 의 계단 위치
    results = []
    for i in range(len(a)):
        if a[i] == b[i]:
            a.append(cnt)
            continue
        elif a[i] == func(b[i]):
            cnt = cnt + 3
        else:
            cnt = cnt - 1
        results.append(cnt);
    return cnt

if __name__ == "__main__":
    a, b = [2,0,0,0,0,0,1,1,0,0], [0,0,0,0,2,2,0,2,2,2]
    print(f'a={a}\nb={b}\nanswer={solution(a,b)}')