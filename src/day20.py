import copy

def part_one(grid: list[list[str]], min_save = 100):
    start = get_starting_position(grid)
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    no_cols = len(grid)
    no_rows = len(grid[0])
    shortest_path = None
    queue = [(start, [start])]
    visited = [start]

    while queue:
        point, hist = queue.pop(0)
        for direction in directions:
            new_point = point[0] + direction[0], point[1] + direction[1]
            if new_point[0] < 0 and new_point[0] >= no_cols \
                and new_point[1] < 0 and new_point[1] >= no_rows:
                continue
            if grid[new_point[1]][new_point[0]] == "#":
                continue
            if grid[new_point[1]][new_point[0]] == "E":
                hist.append(new_point)
                shortest_path = hist
            if new_point not in visited:
                new_hist = copy.copy(hist)
                new_hist.append(new_point)
                visited.append(new_point)
                queue.append((new_point, new_hist))

    # cheat
    total = 0
    for i, point in enumerate(shortest_path):
        for direction in directions:
            new_point = point[0] + direction[0] * 2, point[1] + direction[1] * 2
            if coordinate_within_bounds(grid, new_point) and new_point in shortest_path:
                diff = shortest_path.index(new_point) - i - 2
                if diff >= min_save:
                    total += 1

    return total


def get_starting_position(grid: list[list[str]]) -> tuple:
    start = None
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char == "S":
                start = (x, y)
                break
    return start

def coordinate_within_bounds(grid: list[list[str]], point: tuple) -> bool:
    no_of_rows = len(grid)
    no_of_cols = len(grid[0])
    within_grid = point[0] >= 0 and point[0] < no_of_cols \
        and point[1] >= 0 and point[1] < no_of_rows
    return within_grid


if __name__ == "__main__":
    text = ""
    input_file_path = "input/day20input.txt"
    with open(input_file_path, "r") as f:
        text = f.readlines()
    print("part one: ", part_one(text))