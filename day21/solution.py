from collections import Counter

def parse(lines):
    allergen_dict = {}
    ingredient_counts = Counter()
    for l in lines:
        ingredients, allergens = l.split('(')
        ingredients = ingredients.strip().split(' ')
        allergens = allergens.split('contains')[1].strip()[:-1].split(', ')
        for a in allergens:
            if a not in allergen_dict:
                allergen_dict[a] = set(ingredients)
            else:
                allergen_dict[a] = set(ingredients).intersection(allergen_dict[a])
        ingredient_counts.update(ingredients)
    return allergen_dict, ingredient_counts

def part1(allergen_dict, ingredient_counts):
    all_bads = set()
    for bad_ingredients in allergen_dict.values():
        all_bads = all_bads.union(bad_ingredients)
    return sum(count for ingredient, count in ingredient_counts.items() if ingredient not in all_bads)
    
def part2(allergen_dict, ingredient_counts):
    final_allergen_dict = {}
    while len(final_allergen_dict) < len(allergen_dict):
        for allergen, ingredients in allergen_dict.items():
            if len(ingredients) == 1:
                found_ingredient = ingredients.pop()
                final_allergen_dict[allergen] = found_ingredient
                for ingredients in allergen_dict.values():
                    ingredients.discard(found_ingredient)
    
    return ','.join([j for i, j in list(sorted(final_allergen_dict.items()))])

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
    allergen_dict, ingredient_counts = parse(lines)
    print(part1(allergen_dict, ingredient_counts))
    print(part2(allergen_dict, ingredient_counts))
