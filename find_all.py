def find_all(string, pattern):
    return len([i for i in range(len(string)) if string.startswith(pattern, i)])

if __name__ == "__main__":
    string, pattern = "aBCBCaaaefBCgBC", "BC"
    print(f'string={string}, pattern={pattern}, answer={find_all(string,pattern)}')