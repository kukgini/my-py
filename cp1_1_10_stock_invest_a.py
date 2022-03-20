def solution(prices):
    inf = 1000000001 # 큰수
    tmp = inf        # 큰수 초기값 -> 작은 수를 찾을 때, 구매가
    answer = -inf    # 작은수 초기값 -> 큰 수를 찾을 때, 판매가
    for price in prices:
        if tmp != inf: # 구매한 적이 있다면
            # answer = max(answer, tmp - price)
            answer = max(answer, price - tmp) # 판매가 - 구매가 가 수익
        tmp = min(tmp, price) # 가장 쌀 때 구매가
        print(f'price={price}, answer={answer}')
    return answer # 최대 수익

if __name__ == "__main__":
    prices = [1,2,3]
    print(f'prices={prices}, solution={solution(prices)}')
    prices = [3,1]
    print(f'prices={prices}, solution={solution(prices)}')

