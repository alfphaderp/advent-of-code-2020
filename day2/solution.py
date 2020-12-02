def parse(line):
    nums, policy, passs = line.split(" ")
    num0, num1 = [int(n) for n in nums.split("-")]
    policy = policy[0]
    return num0, num1, policy, passs

def part1(lines):
    def valid(line):
        num0, num1, policy, passs = parse(line)
        return num0 <= passs.count(policy) <= num1
    return sum(valid(l) for l in lines)
    
def part2(lines):
    def valid(line):
        num0, num1, policy, passs = parse(line)
        return (passs[num0 - 1] == policy) ^ (passs[num1 - 1] == policy)
    return sum(valid(l) for l in lines)

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
    print(part1(lines))
    print(part2(lines))
