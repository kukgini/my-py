import cp1_1_05_swarl_matrix_a

def print_matrix(matrix):
    for row in matrix: print(row)

def make_matrix(n):
    m = [[0] * n for _ in range(n)]
    print_matrix(m)
    return m

def solution(n):
    # return cp1_1_05_swarl_matrix_a.solution(n)
    matrix = make_matrix(n)
    distance = n
    row, col = 0, -1
    row_dirs = [0, 1, 0, -1]
    col_dirs = [1, 0, -1, 0]
    dir = 0
    num = 0
    for _ in range(n*2-1):
        for _ in range(distance):
            row += row_dirs[dir]
            col += col_dirs[dir]
            num += 1
            matrix[row][col] = num
        dir = (dir + 1) % 4 # 0,1,2,3 % 4개 방향으로 진행 방향을 바꾼다.
        if divmod(dir,2)[1]: # 2로 나누어 떨어지지 않으면 홀수
            distance -= 1 # col, row 를 한번씩 진행 했으면 1 step 줄인다.
    # print_matrix(matrix)
    answer = 0
    for x in range(n):
        answer += matrix[x][x] # 대각선의 합을 구한다.
    return answer

if __name__ == "__main__":
    input = 2
    print("input=", input, "result=", solution(input));
    input = 3
    print("input=", input, "result=", solution(input));
    input = 4
    print("input=", input, "result=", solution(input));