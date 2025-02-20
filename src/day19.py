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
        mem = dict()
        mem[0] = 1
        for i in range(len(pattern)):
            if not mem.get(i):
                continue
            start_index = i
            times = mem[i]
            for towel in towels:
                end_index = start_index + len(towel)
                if towel == pattern[start_index: end_index]:
                    if old_times := mem.get(end_index):
                        mem[end_index] = old_times + times
                    else:
                        mem[end_index] = times
        if subtotal_times := mem.get(len(pattern)):
            total += subtotal_times
    return total

if __name__ == "__main__":
    input_file_path = "input/day19input.txt"
    text = ""
    with open(input_file_path, "r") as f:
        text = f.read()
    input = parse(text)
    print("result part one: ", part_one(*input))
    print("result part two: ", part_two(*input))