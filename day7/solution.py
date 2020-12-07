from functools import lru_cache

def make_graph(lines):
    graph = {}
    for l in lines:
        first, rest = l.split("contain")
        first = first.strip()
        graph[first] = {}
        for r in rest.split(","):
            r = r.strip()
            if r[:2] != "no":
                qty = int(r[0])
                name = r[1:].strip()
                graph[first][name] = qty
    return graph

def part1(graph):
    @lru_cache(None)
    def contains_shiny(bag):
        if bag == "shiny gold":
            return True
        else:
            return any(contains_shiny(next) for next in graph[bag])
    
    return sum(contains_shiny(bag) for bag in graph) - 1
    
def part2(graph):
    def bags_in(bag):
        if not graph[bag]:
            return 0
        else:
            return sum(count * (1 + bags_in(next)) for next, count in graph[bag].items())
    
    return bags_in("shiny gold")

if __name__ == '__main__':
    with open('input_cleaned.txt', 'r') as f:
        lines = f.read().splitlines()
    graph = make_graph(lines)
    print(part1(graph))
    print(part2(graph))
