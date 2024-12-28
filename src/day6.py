import copy

def part_one(text: str) -> int:
    rows = text.split("\n")
    no_of_cols = len(rows[0])
    no_of_rows = len(rows)

    start_row, start_col = get_starting_pos(rows)
    
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    field = rows
    curr_direction = 0 # (y, x)
    moved_fields = 0
    next_field = (start_row, start_col)
    visited_fields = {next_field}

    while True:
        next_y = next_field[0] + directions[curr_direction][0]
        next_x = next_field[1] + directions[curr_direction][1]
        if next_y < 0 or next_x < 0 or next_y >= no_of_rows or next_x >= no_of_cols:
            break
        if field[next_y][next_x] == "#":
            curr_direction += 1
            curr_direction %= 4
        else:
            next_field = (next_y, next_x)
            visited_fields = visited_fields.union({next_field})
            moved_fields += 1
    return len(visited_fields)

def part_two(text: str) -> int:
    # TODO: improve performance
    rows = text.split("\n")
    no_of_cols = len(rows[0])
    no_of_rows = len(rows)
    
    start_row, start_col = get_starting_pos(rows)

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    field = rows
    curr_direction = 0 # (y, x)
    moved_fields = 0
    next_field = (start_row, start_col)
    visited_fields = {next_field}

    while True:
        next_y = next_field[0] + directions[curr_direction][0]
        next_x = next_field[1] + directions[curr_direction][1]
        if next_y < 0 or next_x < 0 or next_y >= no_of_rows or next_x >= no_of_cols:
            break
        if field[next_y][next_x] == "#":
            curr_direction += 1
            curr_direction %= 4
        else:
            next_field = (next_y, next_x)
            visited_fields = visited_fields.union({next_field})
            moved_fields += 1
    
    result = 0
    for i, point in enumerate(visited_fields):
        # check if obstacle on field turns it into loop
        field_copy = copy.deepcopy(field)
        row = list(field_copy[point[0]])
        row[point[1]] = "#"
        field_copy[point[0]] = "".join(row)
        if check_for_loop(field_copy, start_row, start_col, directions, no_of_rows, no_of_cols):
            result += 1
            print(i, result)
    return result

    
def parse(input_file_path) -> list[str]:
    with open(input_file_path, "r") as f:
        return f.read()
    
def check_for_loop(field, start_y, start_x, directions, no_of_rows, no_of_cols) -> bool:
    next_field = (start_y, start_x)
    path = []
    curr_direction = 0

    while True:
        next_y = next_field[0] + directions[curr_direction][0]
        next_x = next_field[1] + directions[curr_direction][1]
        if stuck_in_loop(path):
            return True
        if next_y < 0 or next_x < 0 or next_y >= no_of_rows or next_x >= no_of_cols:
            break
        if field[next_y][next_x] == "#":
            curr_direction += 1
            curr_direction %= 4
        else:
            next_field = (next_y, next_x)
            path.append((next_field, curr_direction))
    return False

def stuck_in_loop(path: list) -> bool:
    if not path:
        return False
    last_field = path[-1]
    new_path = path[0:-1]
    if last_field in new_path:
        return True
    return False

def get_starting_pos(field: list[str]) -> tuple:
    for y, row in enumerate(field):
        for x, col in enumerate(row):
            if col == "^":
                return y, x
            
if __name__ == "__main__":
    input_file_path = "input/day6input.txt"
    input = parse(input_file_path)
    new_inp = copy.copy(input)
    print("part one: ", part_one(input))
    print("part two: ", part_two(new_inp))