import copy

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

def part_one(map: list[list[str]], start: tuple, end: tuple, history = None) -> tuple:
    no_of_rows = len(map)
    no_of_cols = len(map[0])
    queue = [(start, 0, [start])]
    visited = []
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    if history:
        for point in history:
            if map[point[1]][point[0]] == "#":
                break
        else:
            return len(history), history
    while queue:
        pos, path_len, hist = queue.pop(0)

        if pos == end:
            return path_len, hist

        for direction in directions:
            new_pos = pos[0] + direction[0], pos[1] + direction[1]
            if new_pos[0] >= 0 and new_pos[0] < no_of_cols and \
                new_pos[1] >= 0 and new_pos[1] < no_of_rows \
                and new_pos not in visited and map[new_pos[1]][new_pos[0]] != "#":
                new_hist = copy.copy(hist)
                new_hist.append(new_pos)
                queue.append((new_pos, path_len + 1, new_hist))
                visited.append(new_pos)
    return None, None

def part_two(input: list[list[int]], dimension: int, start: tuple, end: tuple, start_iter: int) -> tuple:
    history = None
    field = build_map(input, start_iter, dimension)
    for i in range(start_iter, len(input)):
        field[input[i][1]][input[i][0]] = "#"
        result, history = part_one(field, start, end, history)
        if not result:
            return input[i]

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
    
    print("result part one: ", part_one(map, start, end)[0])
    print("result part two: ", part_two(input, dimension, start, end, 1024))