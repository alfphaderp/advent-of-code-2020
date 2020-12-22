from collections import deque

def score(winner):
    return sum((len(winner) - i) * winner[i] for i in range(len(winner)))

def part1(p1, p2):
    p1, p2 = deque(p1), deque(p2)
    while len(p1) > 0 and len(p2) > 0:
        if p1[0] > p2[0]:
            p1.append(p1.popleft())
            p1.append(p2.popleft())
        else:
            p2.append(p2.popleft())
            p2.append(p1.popleft())
    return score(p1 if p1 else p2)

def part2(p1, p2):    
    def play(p1, p2):
        p1, p2 = deque(p1), deque(p2)
        seen_states = set()
        while len(p1) > 0 and len(p2) > 0:
            if (tuple(p1), tuple(p2)) in seen_states:
                return "p1", p1
            else:
                seen_states.add((tuple(p1), tuple(p2)))
            
            if len(p1) - 1 >= p1[0] and len(p2) - 1 >= p2[0]:
                round_winner = p1 if play(list(p1)[1:p1[0] + 1], list(p2)[1:p2[0] + 1])[0] == "p1" else p2
            else:
                round_winner = p1 if p1[0] > p2[0] else p2
            
            if round_winner == p1:
                p1.append(p1.popleft())
                p1.append(p2.popleft())
            else:
                p2.append(p2.popleft())
                p2.append(p1.popleft())
        return ("p1", p1) if p1 else ("p2", p2)
        
    return score(play(p1, p2)[1])

def parse(groups):
    return [int(i) for i in groups[0][1:]], [int(i) for i in groups[1][1:]]

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
    p1, p2 = parse(groups)
    print(part1(p1, p2))
    print(part2(p1, p2))
