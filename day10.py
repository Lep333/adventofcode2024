input_file_path = "day10input.txt"

def parse() -> list:
    map = []
    with open(input_file_path, "r") as f:
        map = f.read()
        map = map.split("\n")

    return map

def part_one(map: list) -> int:
    starting_points = get_trail_heads(map)

    row_count = len(map)
    col_count = len(map[0])
    total_routes = 0
    neighbour_directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # calculate all trails
    for y, x in starting_points:
        queue = [(y, x)]
        total_routes += len(set(check_for_trails(map, queue)))
    return total_routes

def part_two(map: list) -> int:
    starting_points = get_trail_heads(map)
    

    total_routes = 0

    # calculate all trails
    for y, x in starting_points:
        queue = [(y, x)]
        total_routes += len(check_for_trails(map, queue))
    return total_routes

def get_trail_heads(map) -> list[(int, int)]:
    starting_points = []
    # scan for starting point
    for y, line in enumerate(map):
        for x, num in enumerate(line):
            if num == "0":
                starting_points.append((y, x))
    return starting_points

def check_for_trails(map, queue) -> list[(int, int)]:
    row_count = len(map)
    col_count = len(map[0])
    neighbour_directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    routes = []
    while queue:
        # check neighbours
        y, x = queue.pop(0)
        current_elevation = int(map[y][x])
        for y_delta, x_delta in neighbour_directions:
            new_y = y + y_delta
            new_x = x + x_delta
            if new_y >= 0 and new_y < row_count and new_x >= 0 and new_x < col_count:
                neighbour_elevation = int(map[new_y][new_x])
                if neighbour_elevation - current_elevation == 1:
                    queue.append((y + y_delta, x + x_delta))
                    if neighbour_elevation == 9:
                        routes.append((y + y_delta, x + x_delta))
    return routes

if __name__ == "__main__":
    map = parse()
    print("total routes: ", part_one(map))
    print("total ratings of all trails: ", part_two(map))