# TODO optimize

NEIGHBORS = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 1),
    (1, -1), (1, 0), (1, 1)
]
ROWS = 0 # updated in __main__ when file is read
COLS = 0

def valid(i, j):
    return i >= 0 and i < ROWS and j >= 0 and j < COLS

def part1(seats):
    def neighbors(r, c, seats):
        count = 0
        for dr, dc in NEIGHBORS:
            if valid(r + dr, c + dc) and seats[r + dr][c + dc] == '#':
                count += 1
        return count

    def update(seats):
        changes = []
        for i in range(ROWS):
            for j in range(COLS):
                if seats[i][j] == 'L' and neighbors(i, j, seats) == 0:
                    changes.append((i, j))
                elif seats[i][j] == '#' and neighbors(i, j, seats) >= 4:
                    changes.append((i, j))
        for i, j in changes:
            seats[i][j] = 'L' if seats[i][j] == '#' else '#'
        return len(changes) > 0
    
    seats = [list(r) for r in seats]
    while update(seats):
        continue
    
    return sum(r.count('#') for r in seats)

def part2(seats):
    def los_neighbors(r, c, seats):
        count = 0
        for dr, dc in NEIGHBORS:
            i, j = r + dr, c + dc
            while valid(i, j) and seats[i][j] == '.':
                i, j = i + dr, j + dc
            if valid(i, j) and seats[i][j] == '#':
                count += 1
        return count

    def los_update(seats):
        changes = []
        for i in range(ROWS):
            for j in range(COLS):
                if seats[i][j] == 'L' and los_neighbors(i, j, seats) == 0:
                    changes.append((i, j))
                elif seats[i][j] == '#' and los_neighbors(i, j, seats) >= 5:
                    changes.append((i, j))
        for i, j in changes:
            seats[i][j] = 'L' if seats[i][j] == '#' else '#'
        return len(changes) > 0
    
    seats = [list(r) for r in seats]
    while los_update(seats):
        continue
    
    return sum(r.count('#') for r in seats)

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
    seats = [list(r) for r in lines]
    ROWS = len(seats)
    COLS = len(seats[0])
    print(part1(seats))
    print(part2(seats))
