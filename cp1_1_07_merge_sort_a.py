def solution(a,b):
    answer = []
    while len(a) > 0 and len(b) > 0:
        if a[0] <= b[0]:
            answer.append(a.pop(0))
        else:
            answer.append(b.pop(0))
    while len(a) > 0:
        answer.append(a.pop(0))
    while len(b) > 0:
        answer.append(b.pop(0))
    return answer

if __name__ == "__main__":
    a = [-2, 3, 5, 9]
    b = [0, 1, 5]
    print(f'answer={solution(a,b)}')