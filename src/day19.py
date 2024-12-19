import copy

def parse(text: str) -> tuple[list[str], list[str]]:
    towels, patterns = text.split("\n\n")
    towels = towels.split(", ")
    patterns = patterns.split("\n")

    return towels, patterns

def pattern_possible(towels: list[str], pattern: str) -> bool:
    stack = [0]
    index_tried = []
    while stack:
        index = stack.pop()
        for towel in towels:
            new_index = index + len(towel)
            slice = pattern[index:new_index]
            if slice == towel:
                if len(pattern) == new_index:
                    return True
                if not new_index in index_tried:
                    stack.append(new_index)
                    index_tried.append(new_index)
    return False
        
def part_one(towels: list[str], patterns: list[str]) -> int:
    total = 0
    for pattern in patterns:
        if pattern_possible(towels, pattern):
            total += 1
    return total

def part_two(towels: list[str], patterns: list[str]) -> int:
    total = 0
    for pattern in patterns:
        stack = [[0]]
        index_tried = []
        possible_variations_from_index = {}
        index_to_sum = []
        while stack:
            el = stack.pop()
            index  = el[-1]
            for towel in towels:
                new_index = index + len(towel)
                slice = pattern[index:new_index]
                if slice == towel:
                    new_el = copy.copy(el)
                    new_el.append(new_index)
                    if len(pattern) == new_index:
                        for ind in new_el:
                            if possible_variations_from_index.get(ind):
                                possible_variations_from_index[ind] += 1
                            else:
                                possible_variations_from_index[ind] = 1
                        continue
                    if not new_index in index_tried:
                        stack.append(new_el)
                        index_tried.append(new_index)
                    else:
                        if possible_variations_from_index.get(new_index):
                            index_to_sum.append(new_el)
        index_to_sum.sort(reverse=True)
        for el in index_to_sum:
            last_el = el[-1] 
            for ind in el:
                if not possible_variations_from_index.get(ind):
                    possible_variations_from_index[ind] = possible_variations_from_index[last_el]
                else:
                    possible_variations_from_index[ind] += possible_variations_from_index[last_el]
        if variation_sum := possible_variations_from_index.get(0):
            total += variation_sum
    return total

if __name__ == "__main__":
    input_file_path = "input/day19input.txt"
    text = ""
    with open(input_file_path, "r") as f:
        text = f.read()
    input = parse(text)
    print("result part one: ", part_one(*input))
    print("result part two: ", part_two(*input))