def part1(lines):
    return sum(len(set("".join(l.split(" ")))) for l in lines)
    
def part2(lines):
    return sum(sum(1 for q in collections.Counter("".join(l.split(" "))).values() if q == len(l.split(" "))) for l in lines)

if __name__ == '__main__':
    with open('input_cleaned.txt', 'r') as f:
        lines = f.read().splitlines()
    print(part1(lines))
    print(part2(lines))
