def solution(prices):
    inf = 1000000001
    tmp = inf
    answer = -inf
    for price in prices:
        if tmp != inf:
            answer = max(answer, tmp - price)
        tmp = min(tmp, price)
    return answer

if __name__ == "__main__":
    prices = [1,2,3]
    print(f'prices={prices}, solution={solution(prices)}')
    prices = [3,1]
    print(f'prices={prices}, solution={solution(prices)}')

