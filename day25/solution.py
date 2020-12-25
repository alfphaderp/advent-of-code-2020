MOD = 20201227
def transform(subject_number, loop_size):
    return pow(subject_number, loop_size, MOD)

def brute_force(public_key):
    i, guess = 0, 1
    while True:
        if guess == public_key:
            return i
        i, guess = i + 1, (guess * 7) % MOD

def part1(lines):
    return transform(int(lines[0]), brute_force(int(lines[1])))

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
    print(part1(lines))
