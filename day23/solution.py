class CLLNode:
    def __init__(self, val):
        self.val = val

class Cups:
    def __init__(self, nums):
        head = CLLNode(nums[0])
        self.access = {nums[0]: head}
        tail = head
        for i in range(1, len(nums)):
            tail.next = CLLNode(nums[i])
            self.access[nums[i]] = tail.next
            tail = tail.next
        tail.next = head
        self.biggest = max(nums)
    
    def find_target(self, start_num, triplet):
        target = self.biggest if start_num == 1 else start_num - 1
        while target in triplet:
            target = self.biggest if target == 1 else target - 1
        return target
    
    def move(self, curr_node=None):
        triplet_head = curr_node.next
        triplet_tail = curr_node.next.next.next
        
        triplet = (triplet_head.val, triplet_head.next.val, triplet_tail.val)
        target = self.access[self.find_target(curr_node.val, triplet)]
        
        curr_node.next = triplet_tail.next
        after_target = target.next
        target.next = triplet_head
        triplet_tail.next = after_target
        return curr_node.next
    
    def simulate(self, start_num, times):
        node = self.access[start_num]
        for _ in range(times):
            node = self.move(node)
    
    def answer_part1(self):
        l = []
        node = self.access[1].next
        while node.val != 1:
            l.append(str(node.val))
            node = node.next
        return ''.join(l)
    
    def answer_part2(self):
        return self.access[1].next.val * self.access[1].next.next.val

def part1(nums):
    c = Cups(nums)
    c.simulate(nums[0], 100)
    return c.answer_part1()
    
def part2(nums):
    i = max(nums) + 1
    while len(nums) < 1000000:
        nums.append(i)
        i += 1
    c = Cups(nums)
    c.simulate(nums[0], 10000000)
    return c.answer_part2()

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
    nums = [int(i) for i in lines[0]]
    print(part1(nums))
    print(part2(nums))
