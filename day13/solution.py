# TODO implement CRT solution

def part1(earliest, ids):
    t = earliest
    while all(t % id != 0 for id in ids.values()):
        t += 1
    return (t - earliest) * min(list(ids.values()), key=lambda id: t % id)
    
def part2(ids):
    base, increment = 1, 1
    for offset, multiple in ids.items():
        while (base + offset) % multiple != 0:
            base += increment
        increment *= multiple
    return base

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
    earliest = int(lines[0]) 
    ids = {i: int(id) for i, id in enumerate(lines[1].split(",")) if id != "x"}
    print(part1(earliest, ids))
    print(part2(ids))
