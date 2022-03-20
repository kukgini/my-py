def solution(arr, K):
    answer = 0
    size = len(arr)
    for i in range(size-2):
        for j in range(i+1, size-1):
            for k in range(j+1, size):
                tot = sum([arr[i], arr[j], arr[k]])
                answer += 1 if tot % K == 0 else 0
                print(f'{arr[i]}, {arr[j]}, {arr[k]}, tot={tot}, answer={answer}')
    return answer

if __name__ == "__main__":
    arr, k = [1,2,3,4,5], 3
    print(f'arr={arr}, k={k}, answer={solution(arr,k)}');