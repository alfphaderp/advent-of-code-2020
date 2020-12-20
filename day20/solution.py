# TODO: kill myself

from collections import defaultdict, Counter
import random

def edges(matrix):
    transform = list(zip(*matrix))
    return [matrix[0], matrix[-1], transform[0], transform[-1]]

def code(edge):
    return int(edge.replace('.', '0').replace('#', '1'), 2)

def invert(edge):
    return ''.join(list(reversed(edge)))

def edge_codes(matrix):
    edge_codes = []
    for e in edges(matrix):
        e = ''.join(e)
        e_i = invert(e)
        edge_codes.append(code(e))
        edge_codes.append(code(e_i))
    return edge_codes

def part1(groups):
    c = defaultdict(lambda: [])
    for g in groups:
        id = int(g[0].split(' ')[1][:-1])
        matrix = [list(row) for row in g[1:]]
        for code in edge_codes(matrix):
            c[code].append(id)
    
    all_edges = []
    for v in c.values():
        if len(v) == 1:
            all_edges.extend(v)
    
    total = 1
    c2 = Counter(all_edges)
    for i, n in c2.items():
        if n == 4:
            total *= i
    
    return total
    
def edge_code_set(matrix):
    s = set()
    for e in edges(matrix):
        e = ''.join(e)
        e_i = invert(e)
        s.add(code(e))
        s.add(code(e_i))
    return s

def potential_neighbors(id_edges, edge_ids, id):
    neighbors = set()
    for edge in id_edges[id]:
        neighbors.update(edge_ids[edge])
    neighbors.discard(id)
    return neighbors

def part2(groups, table):
    id_matrix = {}
    id_edges = {}
    edge_ids = {}
    for g in groups:
        id = int(g[0].split(' ')[1][:-1])
        matrix = [list(row) for row in g[1:]]
        id_matrix[id] = matrix
        id_edges[id] = edge_code_set(matrix)
        for c in id_edges[id]:
            if c not in edge_ids:
                edge_ids[c] = set()
            edge_ids[c].add(id)
    
    aliases = sorted(list(id_matrix.keys()))
    adj_mat = [['0'] * len(aliases) for _ in range(len(aliases))]
    for alias, id in enumerate(aliases):
        for alias2, id2 in enumerate(aliases):
            if id2 in potential_neighbors(id_edges, edge_ids, id):
                adj_mat[alias][alias2] = '1'
    
    # print an adjacency matrix for aliased ids, manually arrange from here
    # for row in adj_mat:
    #     print(','.join(row))
    
    table = [[aliases[int(i)] for i in row.split('\t')] for row in table]
    # for row in table:
    #     print(row)
    
    # print(table[0][0])
    # print_matrix(rotate_times(id_matrix[table[0][0]], 1))
    # print(table[1][0])
    # print_matrix(id_matrix[table[1][0]])
    # print(table[0][1])
    # print_matrix(id_matrix[table[0][1]])
    
    assembly = [[None] * len(table) for _ in range(len(table))]
    
    # figured out through manual testing
    assembly[0][0] = rotate_times(id_matrix[table[0][0]], 1)
    
    # fill out first col
    for i in range(1, len(table)):
        valids = []
        for o in all_orientations(id_matrix[table[i][0]]):
            if verify_ud(assembly[i - 1][0], o):
                valids.append(o)
        assembly[i][0] = random.choice(valids)
        if assembly[i][0] == None:
            print('oh no')
    
    # fill out first row
    for i in range(1, len(table[0])):
        valids = []
        for o in all_orientations(id_matrix[table[0][i]]):
            if verify_lr(assembly[0][i - 1], o):
                valids.append(o)
        assembly[0][i] = random.choice(valids)
        if assembly[0][i] == None:
            print('oh no')
    
    # fill out the rest
    for i in range(1, len(table)):
        for j in range(1, len(table[0])):
            for o in all_orientations(id_matrix[table[i][j]]):
                if verify_lr(assembly[i][j - 1], o) and verify_ud(assembly[i - 1][j], o):
                    assembly[i][j] = o
    
    picture = []
    for row in assembly:
        centerpieces = [get_centerpiece(matrix) for matrix in row]
        for i in range(len(centerpieces[0])):
            picture.append(''.join([''.join(piece[i]) for piece in centerpieces]))
    
    picture_matrix = [list(row) for row in picture]
    monsters = max(find_monsters(o) for o in all_orientations(picture_matrix))
    
    return sum(row.count('#') for row in picture) - monsters * 15

def find_monsters(picture_matrix):
    monster = [
        '                  # ',
        '#    ##    ##    ###',
        ' #  #  #  #  #  #   ',
    ]
    
    def monster_at(i, j):
        for x in range(len(monster)):
            for y in range(len(monster[0])):
                if monster[x][y] == '#' and not picture_matrix[i + x][j + y] == '#':
                    return False
        return True
    
    monster_count = 0
    for i in range(len(picture_matrix) - len(monster) + 1):
        for j in range(len(picture_matrix[0]) - len(monster[0]) + 1):
            if monster_at(i, j):
                monster_count += 1
    return monster_count
    
def get_centerpiece(matrix):
    return [row[1:-1] for row in matrix[1:-1]]

def verify_lr(mat0, mat1):
    return list(zip(*mat0))[-1] == list(zip(*mat1))[0]

def verify_ud(mat0, mat1):
    return mat0[-1] == mat1[0]

def print_matrix(matrix):
    for row in matrix:
        print(''.join(row))
    print()
    
def rotate_times(matrix, times):
    if times == 0:
        return list(matrix)
    else:
        n = len(matrix)
        matrix = [list(row) for row in matrix]
        for _ in range(times):
            for i in range(n // 2):
                for j in range(i, n - i - 1):
                    matrix[i][j], matrix[j][n - 1 - i], matrix[n - 1 - i][n - 1 - j], matrix[n - 1 - j][i] = matrix[j][n - 1 - i], matrix[n - 1 - i][n - 1 - j], matrix[n - 1 - j][i], matrix[i][j]
        return matrix

def flip(matrix, option):
    if option == 0:
        return matrix
    elif option == 1:
        return list(reversed(matrix))
    elif option == 2:
        return [list(reversed(row)) for row in matrix]
    elif option == 3:
        return list(reversed([list(reversed(row)) for row in matrix]))

def all_orientations(matrix):
    orientations = []
    for i in range(4):
        for j in range(4):
            orientations.append(flip(rotate_times(matrix, i), j))
    return orientations

def group(lines):
    groups, group = [], []
    for line in lines:
        if line != "":
            group.append(line)
        else:
            groups.append(group)
            group = []
    groups.append(group)
    return groups

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        groups = group(f.read().splitlines())
    with open('id_table.txt', 'r') as g:
        table = g.read().splitlines()
    print(part1(groups))
    print(part2(groups, table))

