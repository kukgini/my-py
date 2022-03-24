# 0 이 없는 세상

# solution 1)
# number -> string -> list 변환
# list -> string - int 변환
def solution1(num):
    num += 1
    n = list(str(num))
    for i, v in enumerate(n):
        if v == "0":
            n[i] = "1"
    return int("".join(n))

# solution 2)
# comprehension
def solution2(num):
    return ''.join('1' if x == '0' else x for x in str(num+1))


if __name__ == "__main__":
    input = 9949999
    print(f'input={input}, solution1={solution1(input)}')
    print(f'input={input}, solution2={solution2(input)}')