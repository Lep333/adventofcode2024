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
        stack = [0]
        mem = {}
        while stack:
            index = stack.pop()

            for towel in towels:
                next_index = len(towel) + index
                subpattern = pattern[index:next_index]
                if subpattern == towel:
                    if el := mem.get(index):
                        for i, tup in enumerate(el):
                            if tup[0] == subpattern:
                                el[i] = (tup[0], tup[1] + 1)
                                continue
                        else:
                            el.append((subpattern, 1))
                            stack.append(next_index)
                    else:
                        mem[index] = [(subpattern, 1)]
                        stack.append(next_index)



    return total

if __name__ == "__main__":
    input_file_path = "input/day19input.txt"
    text = ""
    with open(input_file_path, "r") as f:
        text = f.read()
    input = parse(text)
    print("result part one: ", part_one(*input))
    print("result part two: ", part_two(*input))