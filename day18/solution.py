# TODO clean up and solve without using eval and regex replaces

def evaluate(tokens):
    total = 0
    sym = None
    for t in tokens:
        if not isinstance(t, tuple) and t in '+*':
            sym = t
        else:
            if isinstance(t, tuple):
                val = evaluate(t)
            else:
                val = int(t)
            
            if sym == '+':
                total += val
            elif sym == '*':
                total *= val
            else:
                total = val
    return total

def evaluate_2(tokens):
    tokens = list(tokens)
    for i in range(len(tokens)):
        if isinstance(tokens[i], tuple):
            tokens[i] = evaluate_2(tokens[i])
    
    new_tokens = [tokens[0]]
    for i in range(1, len(tokens), 2):
        if tokens[i] == '+':
            new_tokens.append(int(new_tokens.pop()) + int(tokens[i + 1]))
        else:
            new_tokens.append(tokens[i])
            new_tokens.append(tokens[i + 1])
    
    total = 1
    for i in range(0, len(new_tokens), 2):
        total *= int(new_tokens[i])
    
    return total
                

def part1(lines):
    return sum(evaluate(eval(l)) for l in lines)
    
def part2(lines):
    return sum(evaluate_2(eval(l)) for l in lines)
    # return sum(evaluate_2(eval(l)) for l in lines)

if __name__ == '__main__':
    # cleaning:
    # ([\d+*]) -> '$1',
    # \) -> ),
    with open('input_cleaned.txt', 'r') as f:
        lines = f.read().splitlines()
    print(part1(lines))
    print(part2(lines))
