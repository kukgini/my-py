def solution(s):
    s = s.lower()
    answer = ""
    previous = s[0]
    counter = 1
    for alphabet in s[1:]:
        if alphabet == previous:
            counter += 1
        else:
            answer += previous + str(counter)
            counter = 1
            previous = s[0]
    answer += previous + str(counter)
    return answer

if __name__ == "__main__":
    s = "YYYYYbbbBbbBBBMmmM"
    print(f's={s}, answer={solution(s)}')