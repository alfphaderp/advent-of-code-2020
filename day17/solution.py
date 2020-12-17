# TODO: clean up and optimize

def part1(lines):
    SIZE = 20

    NEIGHBORS = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                if not (i == j and j == k and k == 0):
                    NEIGHBORS.append((i, j, k))

    def print_cube(cube):
        for layer in cube:
            if sum(row.count('#') for row in layer) > 0:
                for row in layer:
                    print(''.join(row))
                print()

    def neighbors(i, j, k):
        for di, dj, dk in NEIGHBORS:
            yield i + di, j + dj, k + dk

    def active_count(cube):
        return sum(sum(row.count('#') for row in layer) for layer in cube)

    def next_cube(cube):
        new_cube = [[['.'] * SIZE for _ in range(SIZE)] for __ in range(SIZE)]
        for i in range(1, SIZE - 1):
            for j in range(1, SIZE - 1):
                for k in range(1, SIZE - 1):
                    count = 0
                    for ni, nj, nk in neighbors(i, j, k):
                        if cube[ni][nj][nk] == '#':
                            count += 1
                    if cube[i][j][k] == '#' and count != 2 and count != 3:
                        new_cube[i][j][k] = '.'
                    elif cube[i][j][k] == '.' and count == 3:
                        new_cube[i][j][k] = '#'
                    else:
                        new_cube[i][j][k] = cube[i][j][k]
        return new_cube
    
    cube = [[['.'] * SIZE for _ in range(SIZE)] for __ in range(SIZE)]
    initial = [list(l) for l in lines]
    
    length, width = len(initial), len(initial[0])
    for i in range(len(initial)):
        for j in range(len(initial[0])):
            cube[SIZE // 2][i + (SIZE - length) // 2 ][j + (SIZE - width) // 2] = initial[i][j]
    
    for _ in range(6):
        cube = next_cube(cube)
    
    return active_count(cube)

def part2(lines):
    SIZE = 22
    
    NEIGHBORS = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if not (i == j and j == k and k == l and l == 0):
                        NEIGHBORS.append((i, j, k, l))

    def print_cube(cube):
        for hyper in cube:
            for layer in hyper:
                if sum(row.count('#') for row in layer) > 0:
                    for row in layer:
                        print(''.join(row))
                    print()

    def neighbors(i, j, k, l):
        for di, dj, dk, dl in NEIGHBORS:
            yield i + di, j + dj, k + dk, l + dl

    def active_count(cube):
        return sum(sum(sum(row.count('#') for row in layer) for layer in hyper) for hyper in cube)

    def next_cube(cube):
        new_cube = [[[['.'] * SIZE for _ in range(SIZE)] for __ in range(SIZE)] for ___ in range(SIZE)]
        for i in range(1, SIZE - 1):
            for j in range(1, SIZE - 1):
                for k in range(1, SIZE - 1):
                    for l in range(1, SIZE - 1):
                        count = 0
                        for ni, nj, nk, nl in neighbors(i, j, k, l):
                            if cube[ni][nj][nk][nl] == '#':
                                count += 1
                        if cube[i][j][k][l] == '#' and count != 2 and count != 3:
                            new_cube[i][j][k][l] = '.'
                        elif cube[i][j][k][l] == '.' and count == 3:
                            new_cube[i][j][k][l] = '#'
                        else:
                            new_cube[i][j][k][l] = cube[i][j][k][l]
        return new_cube
    
    cube = [[[['.'] * SIZE for _ in range(SIZE)] for __ in range(SIZE)] for ___ in range(SIZE)]
    initial = [list(l) for l in lines]
    
    length, width = len(initial), len(initial[0])
    for i in range(len(initial)):
        for j in range(len(initial[0])):
            cube[SIZE // 2][SIZE // 2][i + (SIZE - length) // 2 ][j + (SIZE - width) // 2] = initial[i][j]
    
    print_cube(cube)
    for i in range(6):
        print('iteration', i)
        cube = next_cube(cube)
    
    return active_count(cube)

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
    print(part1(lines))
    print(part2(lines))
