words = []

def create_words(level, s):
    global words
    vowels = ['A','E','I','O','U']
    words.append(s)
    for i in range(0,5):
        if level < 5:
            create_words(level+1, s+vowels[i])

def solution(word):
    global words
    words = []
    answer = 0
    create_words(0, '')
    for index, i in enumerate(words):
        if word == i:
            answer = index
            break
    return answer

if __name__ == "__main__":
    word = "AAAAE"
    print(f'word={word}, answer={solution(word)}')