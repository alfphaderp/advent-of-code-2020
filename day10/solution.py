from functools import lru_cache
from collections import deque

def part1(nums):
    diffs = [nums[i] - nums[i - 1] for i in range(1, len(nums))]
    return diffs.count(1) * (1 + diffs.count(3))

def part2_recursive(nums):
    @lru_cache(None)
    def dp(i, prev=0):
        if i == len(nums) - 1:
            return 1 if nums[i] - prev <= 3 else 0
        elif nums[i] - prev > 3:
            return 0
        elif nums[i] - prev == 3:
            return dp(i + 1, nums[i])
        else:
            return dp(i + 1, nums[i]) + dp(i + 1, prev)
    return dp(0, 0)
    
def part2_iterative(nums):
    dp = deque([1])
    for i in range(len(nums) - 2, -1, -1):
        print(dp)
        for j in range(i + 1, min(i + 4, len(dp))):
            if nums[j] - nums[i] > 3:
                print("bad")
                dp.pop()
        dp.appendleft(sum(dp))
    print(dp)
    # return sum(dp[i] for i in range(3) if nums[i] <= 3)
    
def part2(nums):
    return part2_iterative(nums)

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
    nums = [int(i) for i in lines]
    nums.sort()
    print(part1(nums))
    print(part2(nums))
