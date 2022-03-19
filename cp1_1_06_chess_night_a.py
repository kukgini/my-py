
def solution(pos):
    # 방법1. ascii code 사용
    # c = ord(pos[0]) - ord('A') # ascii code of A = 65
    # r = ord(pos[1]) - ord('1') # ascii code of 1 = 48

    # 방법2. 좌표 map 사용
    xcords = dict([("A", 0), ("B", 1), ("C", 2), ("D", 3), ("E", 4), ("F", 5), ("G", 6), ("H", 7)])
    ycords = dict([("1", 0), ("2", 1), ("3", 2), ("4", 3), ("5", 4), ("6", 5), ("7", 6), ("6", 7)])
    c = xcords[pos[0]]
    r = ycords[pos[1]]

    moves = [(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,2),(2,-1)]
    answer = 0
    for move in moves:
        posr = move[0]
        posc = move[1]
        print(posr, posc)
        if posr >= 0 and posr < 8 and posc >= 0 and posc < 8:
            answer += 1
    return answer

if __name__  == "__main__":
    print(f'answer={solution("A7")}')