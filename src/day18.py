import math

def build_map(input: list[list[int]], falling_onto_mem: int, dimension: int) -> list[list[str]]:
    map = []
    for y in range(dimension):
        row = []
        for x in range(dimension):
            row.append(".")
        map.append(row)

    for i in range(falling_onto_mem):
        map[input[i][1]][input[i][0]] = "#"
    return map

def part_one(map: list[list[str]], start: tuple, end: tuple) -> tuple:
    no_of_rows = len(map)
    no_of_cols = len(map[0])
    queue = [(start, 0)]
    visited = []
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    while queue:
        pos, path_len = queue.pop(0)

        if pos == end:
            return path_len

        for direction in directions:
            new_pos = pos[0] + direction[0], pos[1] + direction[1]
            if new_pos[0] >= 0 and new_pos[0] < no_of_cols and \
                new_pos[1] >= 0 and new_pos[1] < no_of_rows \
                and new_pos not in visited and map[new_pos[1]][new_pos[0]] != "#":
                queue.append((new_pos, path_len + 1))
                visited.append(new_pos)

def part_two(input: list[list[int]], dimension: int, start: tuple, end: tuple, start_iter: int) -> tuple:
    field = build_map(input, start_iter, dimension)
    upper = len(input)
    lower = 0
    i = math.floor(len(input) / 2)
    next_iter = 0
    while True:
        field = build_map(input, i, dimension)
        result = part_one(field, start, end)
        if not result:
            upper = i
            next_iter = i - math.floor((upper - lower) / 2)
        else:
            lower = i
            next_iter = i + math.floor((upper - lower) / 2)
        if i == next_iter:
            return input[i]
        i = math.floor(next_iter)

if __name__ == "__main__":
    input_file_path = "input/day18input.txt"
    input = []
    with open(input_file_path, "r") as f:
        input = f.read()
    input = input.split("\n")
    for i, line in enumerate(input):
        input[i] = list(map(int, line.split(",")))
    dimension = 71
    map = build_map(input, 1024, dimension)
    start = (0, 0)
    end = (70, 70)
    dimension = 71
    
    print("result part one: ", part_one(map, start, end))
    print("result part two: ", part_two(input, dimension, start, end, 1024))