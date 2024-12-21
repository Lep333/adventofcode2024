import copy

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def part_one(grid: list[list[str]], min_save = 100):
    start = get_position_of_char(grid, "S")
    end = get_position_of_char(grid, "E")
    shortest_path = get_shortest_path(grid, start, end)
    return find_cheats(grid, shortest_path, min_save)

def part_two(grid: list[list[str]], min_save = 100) -> int:
    start = get_position_of_char(grid, "S")
    end = get_position_of_char(grid, "E")
    shortest_path = get_shortest_path(grid, start, end)
    return find_cheats2(grid, shortest_path, min_save)

def get_shortest_path(grid: list[list[str]], start: tuple, end: tuple, cheat=False) -> list[tuple]:
    no_cols = len(grid)
    no_rows = len(grid[0])
    shortest_path = None
    queue = [(start, [start])]
    visited = [start]
    while queue:
        point, hist = queue.pop(0)
        for direction in directions:
            new_point = point[0] + direction[0], point[1] + direction[1]
            if not coordinate_within_bounds(grid, point):
                continue
            if not cheat and grid[new_point[1]][new_point[0]] == "#":
                continue
            if new_point[0] == end[0] and new_point[1] == end[1]:
                hist.append(new_point)
                shortest_path = hist
            if new_point not in visited:
                new_hist = copy.copy(hist)
                new_hist.append(new_point)
                visited.append(new_point)
                queue.append((new_point, new_hist))
    return shortest_path

def get_position_of_char(grid: list[list[str]], char_to_find: str) -> tuple:
    start = None
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char == char_to_find:
                start = (x, y)
                break
    return start

def coordinate_within_bounds(grid: list[list[str]], point: tuple) -> bool:
    no_of_rows = len(grid)
    no_of_cols = len(grid[0])
    within_grid = point[0] >= 0 and point[0] < no_of_cols \
        and point[1] >= 0 and point[1] < no_of_rows
    return within_grid

def find_cheats(grid: list[list[str]], shortest_path: list[tuple], min_save: int) -> int:
    total = 0
    for i, point in enumerate(shortest_path):
        for direction in directions:
            new_point = point[0] + direction[0] * 2, point[1] + direction[1] * 2
            if coordinate_within_bounds(grid, new_point) and new_point in shortest_path:
                diff = shortest_path.index(new_point) - i - 2
                if diff >= min_save:
                    total += 1
    return total


def find_cheats2(grid: list[list[str]], shortest_path: list[tuple], min_save: int) -> int:
    # search for nearby fields that are in path
    cheat_length = 20
    total = 0
    for i, point in enumerate(shortest_path):
        for target_point in get_nearby_points_on_path(grid, shortest_path, point, cheat_length):
            diff_x = abs(point[0] - target_point[0])
            diff_y = abs(point[1] - target_point[1])
            diff = diff_x + diff_y
            diff = shortest_path.index(target_point) - i - diff
            if i < shortest_path.index(target_point) and diff >= min_save:
                total += 1

    return total


def get_nearby_points_on_path(grid: list[list[str]],
    shortest_path: list[tuple], start: tuple[int], distance: int) -> list[tuple]:
    nearest_points = []
    for target_point in shortest_path:
        if start == target_point:
            continue
        diff_x = abs(start[0] - target_point[0])
        diff_y = abs(start[1] - target_point[1])
        if diff_x + diff_y <= distance:
            nearest_points.append(target_point)
    return nearest_points

if __name__ == "__main__":
    text = ""
    input_file_path = "input/day20input.txt"
    with open(input_file_path, "r") as f:
        text = f.readlines()
    print("part one: ", part_one(text))
    print("part two: ", part_two(text))