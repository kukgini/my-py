def solution(a,b):
    a_index = 0
    b_index = 0
    a_size = len(a)
    b_size = len(b)
    answer = []
    while a_index < a_size and b_index < b_size:
        if (a[a_index] < b[b_index]):
            answer.append(a[a_index])
            a_index += 1
        else:
            answer.append(b[b_index])
            b_index += 1
    while a_index < a_size:
        answer.append(a[a_index])
        a_index += 1
    while b_index < b_size:
        answer.append(b[b_index])
        b_index += 1
    return answer

if __name__ == "__main__":
    a = [-2, 3, 5, 9]
    b = [0, 1, 5]
    print(f'answer={solution(a,b)}')