def part1(lines):
    s = set()
    for i in range(len(lines)):
        n = int(lines[i])
        target = 2020 - n
        if target in s:
            return n * target
        s.add(n)
    
def part2(lines):
    s = set()
    for i in range(len(lines)):
        n0 = int(lines[i])
        for j in range(i + 1, len(lines)):
            n1 = int(lines[j])
            target = 2020 - n0 - n1
            if target in s:
                return n0 * n1 * target
        s.add(n0)

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
    print(part1(lines))
    print(part2(lines))
