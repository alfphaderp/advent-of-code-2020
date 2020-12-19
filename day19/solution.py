# TODO clean up

import re

def parse(groups):
    rules = {}
    for r in groups[0]:
        tokens = r.split(':')
        rule_num = int(tokens[0])
        stripped_tokens = tokens[1].strip()
        if stripped_tokens[0] == '"':
            rule = stripped_tokens[1]
        else:
            matches = stripped_tokens.split('|')
            rule = [[int(i) for i in m.strip().split(' ')] for m in matches]
        rules[rule_num] = rule
    
    return rules, groups[1]
        
def get_regexes(rules):
    def get_regex_str(rule_num):
        if isinstance(rules[rule_num], str):
            return rules[rule_num]
        else:
            sub_regexes = []
            for match in rules[rule_num]:
                sub_regexes.append(''.join([get_regex_str(option) for option in match]))
            return '(' + '|'.join(sub_regexes) + ')'
    
    return {i: re.compile('^' + get_regex_str(i) + '$') for i in rules.keys()}

def part1(groups):
    rules, messages = parse(groups)
    
    regexes = get_regexes(rules)
    
    return sum(bool(regexes[0].match(m)) for m in messages)
    
def get_regexes_p2(rules):
    def get_regex_str(rule_num):
        if isinstance(rules[rule_num], str):
            return rules[rule_num]
        elif rule_num == 8:
            return '(' + get_regex_str(42) + ')+'
        elif rule_num == 11:
            forty_two, thirty_one = get_regex_str(42), get_regex_str(31)
            
            sub_regexes = []
            for i in range(1, 50):
                sub_regexes.append(forty_two * i + thirty_one * i)
            return '(' + '|'.join(sub_regexes) + ')'
        else:
            sub_regexes = []
            for match in rules[rule_num]:
                sub_regexes.append(''.join([get_regex_str(option) for option in match]))
            return '(' + '|'.join(sub_regexes) + ')'
    
    return {i: re.compile('^' + get_regex_str(i) + '$') for i in rules.keys()}
    
def part2(groups):
    rules, messages = parse(groups)
    regexes = get_regexes_p2(rules)
    return sum(bool(regexes[0].match(m)) for m in messages)

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
