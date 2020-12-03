def count_trees(lines, dx, dy):
    col = 0
    total = 0
    for i in range(0, len(lines), dy):
        if lines[i][col] == "#":
            total += 1
        col = (col + dx) % len(lines[0])
    return total

def part1(lines):
    return count_trees(lines, 3, 1)
    
def part2(lines):
    product = 1
    for dx, dy in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        product *= count_trees(lines, dx, dy)
    return product

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
    print(part1(lines))
    print(part2(lines))
