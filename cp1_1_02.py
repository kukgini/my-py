
def leftPad(string, length):
    padZero = ""
    padSize = abs(len(string)-length) # 3,5 = 2
    print(f'padSize={padSize}')
    for i in range(padSize):
        padZero += "0"
    return padZero + string

def solution(binaryA, binaryB):
    max_length = max(len(binaryA), len(binaryB))
    binaryA = leftPad(binaryA, max_length)
    binaryB = leftPad(binaryB, max_length)

    hamming_distance = 0
    for i in range(max_length):
        if binaryA[i] != binaryB[i]:
            hamming_distance += 1;
    return hamming_distance


if __name__ == "__main__":
    ret = solution("10010","110")
    print(ret)