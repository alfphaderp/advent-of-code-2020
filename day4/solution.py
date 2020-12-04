def get_dict(fields):
    return {f.split(":")[0]: f.split(":")[1] for f in fields}

def part1(lines):
    return sum(p1_valid(get_dict(l.split(" "))) for l in lines)

def p1_valid(field_dict):
    good_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    return sum([key in field_dict for key in good_keys]) == 7

def part2(lines):
    return sum(p2_valid(get_dict(l.split(" "))) for l in lines)

def p2_valid(field_dict):
    return \
        p1_valid(field_dict) and \
        1920 <= int(field_dict["byr"]) <= 2002 and \
        2010 <= int(field_dict["iyr"]) <= 2020 and \
        2020 <= int(field_dict["eyr"]) <= 2030 and \
        validate_hgt(field_dict["hgt"]) and \
        validate_hcl(field_dict["hcl"]) and \
        field_dict["ecl"] in "amb blu brn gry grn hzl oth" and \
        len(field_dict["pid"]) == 9

def validate_hgt(hgt):
    return (hgt[-2:] == "cm" and 150 <= int(hgt[:-2]) <= 193) or \
        (hgt[-2:] == "in" and 59 <= int(hgt[:-2]) <= 76)
    
def validate_hcl(hcl):
    return hcl[0] == "#" and all(c in "0123456789abcdef" for c in hcl[1:])

if __name__ == '__main__':
    # manually preprocessed to group entries together and remove blank lines
    # replaced (.)\r\n(.) with $1 $2
    # then replaced \r\n\r\n with \r\n
    with open('input_cleaned.txt', 'r') as f:
        lines = f.read().splitlines()
    print(part1(lines))
    print(part2(lines))
