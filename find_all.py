def find_all(string, pattern):
    return len([i for i in range(len(string)) if string.startswith(pattern, i)])