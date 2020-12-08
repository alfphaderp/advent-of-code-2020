def instructions(lines):
    return [[l.split(" ")[0], int(l.split(" ")[1])] for l in lines]

def run(ins):
    acc, iptr, seen = 0, 0, set()
    while iptr not in seen and iptr < len(ins):
        curr = ins[iptr]
        seen.add(iptr)        
        if curr[0] == "acc":
            acc += curr[1]
            iptr += 1
        elif curr[0] == "jmp":
            iptr += curr[1]
        else:
            iptr += 1
    
    return iptr == len(ins), acc

def part1(ins):
    return run(ins)[1]
    
def part2(ins):
    def test(i):
        temp = ins[i]
        ins[i] = "jmp" if temp[0] == "nop" else "nop"
        result = run(ins)
        ins[i] = temp
        return result[1] if result[0] else None
        
    for i in range(len(ins)):
        result = test(i)
        if result:
            return result

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
    ins = instructions(lines)
    print(part1(ins))
    print(part2(ins))
