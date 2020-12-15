# TODO: clean up

from itertools import combinations

def to_bin(i):
    return format(i, '036b')

def to_int(b):
    return int(b, 2)

def simulate(lines, func):
    mem = {}
    for l in lines:
        s = l.split(' ')
        if s[0] == 'mask':
            mask = s[-1]
        else:
            address = int(s[0][4:-1])
            value = int(s[-1])
            func(mem, mask, address, value)
    
    return sum(mem.values())

def part1(lines):
    def mask_value(value, mask):
        return to_int(''.join([value[i] if mask[i] == 'X' else mask[i] for i in range(36)]))
    
    def set_mem(mem, mask, address, value):
        mem[address] = mask_value(to_bin(value), mask)
    
    return simulate(lines, set_mem)

def part2(lines):
    def mask_address(address, mask):
        return ''.join([address[i] if mask[i] == '0' else mask[i] for i in range(36)])
    
    def all_addresses(address, mask):
        masked_address = mask_address(address, mask)
        index_powers = [2 ** i for i, b in enumerate(reversed(masked_address)) if b == 'X']
        base = to_int(masked_address.replace('X', '0'))
        addresses = []
        for i in range(len(index_powers) + 1):
            for sublist in combinations(index_powers, i):
                addresses.append(base + sum(sublist))
        return addresses
    
    def set_mem(mem, mask, address, value):
        for a in all_addresses(to_bin(address), mask):
            mem[a] = value
    
    return simulate(lines, set_mem)

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
    print(part1(lines))
    print(part2(lines))
