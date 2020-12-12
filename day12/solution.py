DIRECTIONS = [(1, 0), (0, -1), (-1, 0), (0, 1)]

def part1(lines):
    x, y, dir = 0, 0, 0
    for ins in lines:
        act, amt = ins[0], int(ins[1:])
        if act == 'N':
            y += amt
        elif act == 'S':
            y -= amt
        elif act == 'E':
            x += amt
        elif act == 'W':
            x -= amt
        elif act == 'L':
            dir = (dir - (amt // 90)) % 4
        elif act == 'R':
            dir = (dir + (amt // 90)) % 4
        elif act == 'F':
            dx, dy = DIRECTIONS[dir]
            x, y = x + dx * amt, y + dy * amt
    return abs(x) + abs(y)

def part2(lines):
    x, y, dir = 0, 0, 0
    way_x, way_y = 10, 1
    for ins in lines:
        act, amt = ins[0], int(ins[1:])
        if act == 'N':
            way_y += amt
        elif act == 'S':
            way_y -= amt
        elif act == 'E':
            way_x += amt
        elif act == 'W':
            way_x -= amt
        elif act == 'L':
            for _ in range(amt // 90):
                way_x, way_y = -way_y, way_x
        elif act == 'R':
            for _ in range(amt // 90):
                way_x, way_y = way_y, -way_x
        elif act == 'F':
            x, y = x + way_x * amt, y + way_y * amt
    return abs(x) + abs(y)
    
if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
    print(part1(lines))
    print(part2(lines))
