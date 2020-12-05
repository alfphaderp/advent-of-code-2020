def id(code):
    return int(code.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1"), 2)

def part1(lines):
    return max(id(code) for code in lines)
    
def part2(lines):
    ids = set(id(code) for code in lines)
    for i in ids:
        if i + 1 not in ids and i + 2 in ids:
            return i + 1

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
    print(part1(lines))
    print(part2(lines))
