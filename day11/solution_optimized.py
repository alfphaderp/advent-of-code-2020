NEIGHBORS = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 1),
    (1, -1), (1, 0), (1, 1)
]
ROWS = 0 # updated in __main__ when file is read
COLS = 0

def is_valid(i, j):
    return i >= 0 and i < ROWS and j >= 0 and j < COLS

def count_occupied(seats, coords):
    return [seats[i][j] for i, j in coords].count('#')

def simulate(seats, neighbor_func, tolerance):
    neighbors = [[neighbor_func(i, j) for j in range(COLS)] for i in range(ROWS)]
    
    def update(seats, coords):
        unstable_coords = set()
        updates = []
        for i, j in coords:
            occupied = count_occupied(seats, neighbors[i][j])
            if seats[i][j] == 'L' and occupied == 0:
                updates.append((i, j, '#'))
                unstable_coords.update(neighbors[i][j])
            elif seats[i][j] == '#' and occupied >= tolerance:
                updates.append((i, j, 'L'))
                unstable_coords.update(neighbors[i][j])
        for i, j, val in updates:
            seats[i][j] = val
        return unstable_coords
    
    coords = [(i, j) for i in range(ROWS) for j in range(COLS)]
    seats = [list(r) for r in seats]
    while coords:
        coords = update(seats, coords)
    
    return sum(r.count('#') for r in seats)

def part1(seats):
    def find_neighbors(r, c):
        neighbors = []
        for dr, dc in NEIGHBORS:
            i, j = r + dr, c + dc
            if is_valid(i, j) and seats[i][j] != '.':
                neighbors.append((i, j))
        return neighbors
    
    return simulate(seats, find_neighbors, 4)

def part2(seats):
    def find_los_neighbors(r, c):
        neighbors = []
        for dr, dc in NEIGHBORS:
            i, j = r + dr, c + dc
            while is_valid(i, j) and seats[i][j] == '.':
                i, j = i + dr, j + dc
            if is_valid(i, j):
                neighbors.append((i, j))
        return neighbors
    
    return simulate(seats, find_los_neighbors, 5)

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
    seats = [list(r) for r in lines]
    ROWS = len(seats)
    COLS = len(seats[0])
    print(part1(seats))
    print(part2(seats))
