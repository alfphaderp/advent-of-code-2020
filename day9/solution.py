def part1(nums):
    def verify(nums, target):
        s = set()
        for n in nums:
            if target - n in s:
                return True
            else:
                s.add(n)
        return False
    for i in range(25, len(nums)):
        if not verify(nums[i - 25:i], nums[i]):
            return nums[i]

def part2(nums):
    def find_range(nums, target):
        lptr, rptr, total = 0, 0, 0
        while rptr < len(lines):
            if total < target:
                total += nums[rptr]
                rptr += 1
            elif total > target:
                total -= nums[lptr]
                lptr += 1
            else:
                return nums[lptr:rptr]
    r = find_range(nums, part1(nums))
    return min(r) + max(r)

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
    nums = [int(i) for i in lines]
    print(part1(nums))
    print(part2(nums))
