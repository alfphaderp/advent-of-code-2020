from functools import lru_cache

def parse(groups):
    fields = {}
    all_ranges = set()
    for f in groups[0]:
        name, ranges = f.split(':')
        ranges = [[int(b) for b in r.split('-')] for r in ranges.split('or')]
        fields[name] = [range(r[0], r[1] + 1) for r in ranges]
        for r in fields[name]:
            all_ranges.update(list(r))
    
    your_ticket = [int(i) for i in groups[1][1].split(',')]
    nearby_tickets = [[int(i) for i in t.split(',')] for t in groups[2][1:]]
    
    return fields, all_ranges, your_ticket, nearby_tickets

def part1(groups):
    fields, all_ranges, your_ticket, nearby_tickets = parse(groups)
    return sum(sum(v for v in t if v not in all_ranges) for t in nearby_tickets)

def part2(groups):
    fields, all_ranges, your_ticket, nearby_tickets = parse(groups)
    
    good_tickets = [t for t in nearby_tickets if all(v in all_ranges for v in t)]
    good_tickets.append(your_ticket)
    
    possible_fields = [set() for _ in range(len(fields))]
    for i in range(len(fields)):
        for f in fields:
            r0, r1 = fields[f][0], fields[f][1]
            if all(row[i] in r0 or row[i] in r1 for row in good_tickets):
                possible_fields[i].add(f)
    
    field_order = [None] * len(fields)
    for _ in range(len(fields)):
        for i in range(len(fields)):
            if len(possible_fields[i]) == 1:
                field_order[i] = possible_fields[i].pop()
                for f in possible_fields:
                    f.discard(field_order[i])
    
    total = 1
    for i in range(len(fields)):
        if field_order[i].split(' ')[0] == 'departure':
            total *= your_ticket[i]
    
    return total

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
    print(part1(groups))
    print(part2(groups))
