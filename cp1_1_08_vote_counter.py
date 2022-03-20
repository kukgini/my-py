def solution(n, votes):
    vote_counter = [0 for i in range(n+1)]
    # 각 후보가 몇 표를 받았는지 개수를 세는 것
    for i in votes:
        vote_counter[i] += 1
    # 표의 수 중에서 최대
    max_val = max(vote_counter)
    print(f'vote_counter={vote_counter}, max_val={max_val}')
    answer = []
    for idx in range(1, n + 1):
        if vote_counter[idx] == max_val:
            answer.append(vote_counter[idx])
    return answer

if __name__ == "__main__":
    votes = [1,5,4,3,2,5,2,5,5,4]
    print(f'votes={votes}, answer={solution(5, votes)}')
    votes = [1,3,2,3,2]
    print(f'votes={votes}, answer={solution(3, votes)}')