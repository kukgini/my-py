# 연속해서 증가하는 가장 긴 구간의 길이

def solution(arr):
    answer = 0
    prev = arr[0]
    cnt = 1
    max_cnt = 1
    for curr in arr[1:]:
        print(f'prev={prev}, curr={curr}')
        if curr > prev:
            cnt += 1
        else:
            max_cnt = max(cnt, max_cnt)
            cnt = 1
            print('reset')
        prev = curr
    answer = max_cnt
    return answer

if __name__ == "__main__":
    arr = [3,1,2,4,5,1,2,2,3,4]
    print(f'arr={arr}, result should be 4, answer={solution(arr)}')