# TODO: redo the whole thing with a sensible coordinates, also clean up

from collections import Counter, defaultdict
from math import sqrt

S3O2 = int(round((sqrt(3) / 2), 4) * 1000)

def to_2d(triplet):
    x, y = 1000 * triplet[0], 0
    x += 500 * triplet[1]
    y += S3O2 * triplet[1]
    x += -500 * triplet[2]
    y += S3O2 * triplet[2]
    return (x, y)

def to_triplet(line):
    triplet = [0, 0, 0]
    i = 0
    while i < len(line):
        if line[i] == 'e' or line[i] == 'w':
            triplet[0] += 1 if line[i] == 'e' else -1
            i += 1
        elif line[i:i + 2] == 'ne' or line[i:i + 2] == 'sw':
            triplet[1] += 1 if line[i:i + 2] == 'ne' else -1
            i += 2
        elif line[i:i + 2] == 'nw' or line[i:i + 2] == 'se':
            triplet[2] += 1 if line[i:i + 2] == 'nw' else -1
            i += 2
    return triplet

def initial_state(lines):
    c = Counter([to_2d(to_triplet(l)) for l in lines])
    for k, v in c.items():
        c[k] = v % 2
    return c

def count_blacks(state):
    return sum(v % 2 for v in state.values())

def part1(lines):
    return count_blacks(initial_state(lines))

def neighbors(t):
    x, y = t[0], t[1]
    neighbors = []
    for dx, dy in [(1000, 0), (-1000, 0), (500, S3O2), (500, -S3O2), (-500, S3O2), (-500, -S3O2)]:
        neighbors.append((x + dx, y + dy))
    return neighbors

def black_neighbors(t, state):
    return sum(state[n] for n in neighbors(t))

ALL_TILES = set([(0, 0)])
for _ in range(100):
    for t in list(ALL_TILES):
        ALL_TILES.update(neighbors(t))
def next_state(state):
    new_state = defaultdict(lambda: 0)
    for t in ALL_TILES:
        count = black_neighbors(t, state)        
        if state[t] == 1:
            if not (count == 0 or count > 2):
                new_state[t] = 1
        else:
            if count == 2:
                new_state[t] = 1
            
    return new_state

def print_state(state):
    print([t for t, v in state.items() if v == 1])
    pass

def simulate(initial_state, times):
    for _ in range(times):
        initial_state = next_state(initial_state)
    return initial_state

def part2(lines):
    return count_blacks(simulate(initial_state(lines), 100))
    
if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
    print(part1(lines))
    print(part2(lines))
