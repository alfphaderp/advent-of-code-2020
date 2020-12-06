def part1(lines):
    total = 0
    for group in lines:
        responses = group.split(" ")
        all = set()
        for r in responses:
            all = all.union(set(r))
        total += len(all)
    return total
    
def part2(lines):
    total = 0
    for group in lines:
        responses = group.split(" ")
        all = set("abcdefghijklmnopqrstuvwxyz")
        for r in responses:
            all = all.intersection(set(r))
        total += len(all)
    return total

if __name__ == '__main__':
    with open('input_cleaned.txt', 'r') as f:
        lines = f.read().splitlines()
    print(part1(lines))
    print(part2(lines))
