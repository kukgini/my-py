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
    return ''.join('1' if x == '0' else x for x in str(num))


if __name__ == "__main__":
    input = 9949999
    ret = solution2(input)
    print("solution2 result=", ret);