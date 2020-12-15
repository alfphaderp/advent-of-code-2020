# TODO: go sublinear?

def find(start, ordinal):
    last_seen = {n: [i] for i, n in enumerate(start)}
    num = start[-1]
    for i in range(len(start), ordinal):
        if len(last_seen[num]) == 1:
            num = 0
        else:
            num = last_seen[num][-1] - last_seen[num][-2]
        nums.append(num)
        if num not in last_seen:
            last_seen[num] = [i]
        elif len(last_seen[num]) == 1:
            last_seen[num].append(i)
        else:
            last_seen[num][0], last_seen[num][1] = last_seen[num][1], i
    return num

def part1(nums):
    return find(nums, 2020)

def part2(nums):
    return find(nums, 30000000)

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
    nums = [int(i) for i in lines[0].split(',')]
    print(part1(nums))
    print(part2(nums))
