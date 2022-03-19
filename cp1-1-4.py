# number -> string -> list 변환
# list -> string - int 변환

def solution(num):
    num += 1
    n = list(str(num))
    for i, v in enumerate(n):
        if v == "0":
            n[i] = "1"
    return int("".join(n))

if __name__ == "__main__":
    input = 9949999
    ret = solution(input)
    print("result=", ret);