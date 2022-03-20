def solution(commands):
    directions = dict(zip("LRUD", [[-1,0],[1,0],[0,1],[0,-1]]))
    x, y = 0,0
    for command in commands:
        dir = directions[command]
        x,y = x + dir[0], y + dir[1]
    return [x,y]

if __name__ == "__main__":
    commands = "URDDL"
    print(f'commands={commands}, answer={solution(commands)}')
    commands = "LRUD"
    print(f'commands={commands}, answer={solution(commands)}')
    commands = ""
    print(f'commands={commands}, answer={solution(commands)}')
