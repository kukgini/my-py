# 비숍 위치가 주어졌을 때 한번에 잡히지 않도록 체스 말을 놓을 수 있는 빈칸 갯수 반환
# 예:
# [D5] ==> 50
# [D5, E8, G2] => 42
#
# 힌트: ord 는 ascii code 를 반환해 줌

def code_to_pos(code):
    x = ord(code[0]) - ord('A') # A = 0, B = 1, ..., H = 7
    y = int(code[1]) - 1        # board 의 좌표가 0 부터 시작하므로 1다 을 뺀다.
    return (y, x)

def move(board, position, direction):
    print(f'move to {position}')
    if 0 <= position[0] < 8 and 0 <= position[1] < 8:
        board[position[0]][position[1]] = 0
        next = (position[0] + direction[0], position[1] + direction[1])
        move(board, next, direction)
    else:
        print('end of move')

def make_board(n):
    board = [[1]*n for _ in range(8)]
    print_board(board)
    return board

def print_board(board):
    for row in board: print(row)

def solution(bishops):
    board = make_board(8)
    directions = [[1,1], [-1,1], [-1,-1], [1,-1]]
    for bishop in bishops:
        print(f'bishop={bishop}')
        for direction in directions:
            move(board, code_to_pos(bishop), direction)
    print_board(board)
    return sum([sum(x) for x in board])

if __name__ == "__main__":
    bishops = ["D5","E8","G2"]
    print(f'bishops={bishops}, answer={solution(bishops)}')
    bishops = ["D5"]
    print(f'bishops={bishops}, answer={solution(bishops)}')