import copy

input_file_path = "input/day15input.txt"

def parse(file_path: str) -> tuple:
    text = ""
    with open(file_path, "r") as f:
        text = f.read()
    field, instructions = text.split("\n\n")
    field = field.split()
    return field, instructions

def part_one(input: tuple) -> int:
    map = copy.deepcopy(input[0])
    
    # directions x, y
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    # move robo
    for char in input[1]:
        robo_pos = find_robot(map)
        if char == ">":
            target_field = move_target(map, robo_pos, directions[0])
            if target_field:
                map = execute_move(map, robo_pos, target_field, directions[0])
        if char == "v":
            target_field = move_target(map, robo_pos, directions[1])
            if target_field:
                map = execute_move(map, robo_pos, target_field, directions[1])
        if char == "<":
            target_field = move_target(map, robo_pos, directions[2])
            if target_field:
                map = execute_move(map, robo_pos, target_field, directions[2])
        if char == "^":
            target_field = move_target(map, robo_pos, directions[3])
            if target_field:
                map = execute_move(map, robo_pos, target_field, directions[3])
    
    # calculate result
    result = 0
    for y, row in enumerate(map):
        for x, char in enumerate(row):
            if char == "O":
                result += y * 100 + x
    return result

def find_robot(map: list[str]):
    for y, row in enumerate(map):
        for x, char in enumerate(row):
            if char == "@":
                return (x, y)

def move_target(map: list[str], robo_pos: tuple, direction: tuple) -> int:
    no_rows = len(map)
    no_cols = len(map[0])
    i = 1
    while True:
        new_pos = robo_pos[0] + direction[0] * i, robo_pos[1] + direction[1] * i
        if direction[0] and i >= no_cols:
            return None
        if direction[1] and i >= no_rows:
            return None
        if map[new_pos[1]][new_pos[0]] == "#":
            return None
        if map[new_pos[1]][new_pos[0]] == ".":
            return i
        i += 1

def execute_move(map: list[str], robo_pos: tuple, target_field: int, direction: tuple) -> list[str]:
    el_to_move = ()
    for i in range(target_field, 0, -1):
        if direction[0]:
            el_to_move = map[robo_pos[1]][robo_pos[0] + direction[0] * i]
            el = map[robo_pos[1]][robo_pos[0] + direction[0] * i - direction[0]]
            row = list(map[robo_pos[1]])
            row[robo_pos[0] + direction[0] * i] = el
            row[robo_pos[0] + direction[0] * i - direction[0]] = el_to_move
            map[robo_pos[1]] = ''.join(row)
        else:
            el_to_move = map[robo_pos[1] + direction[1] * i][robo_pos[0]]
            el = map[robo_pos[1] + direction[1] * i - direction[1]][robo_pos[0]]
            row = list(map[robo_pos[1] + direction[1] * i])
            row[robo_pos[0]] = el
            other_row = list(map[robo_pos[1] + direction[1] * i - direction[1]])
            other_row[robo_pos[0]] = el_to_move
            map[robo_pos[1] + direction[1] * i] = ''.join(row)
            map[robo_pos[1] + direction[1] * i - direction[1]] = ''.join(other_row)
    return map

def part_two(input: tuple) -> int:
    # scale up map
    new_map = []
    for row in input[0]:
        row_str = ""
        for char in row:
            if char in ["#", "."]:
                row_str += char * 2
            if char == "@":
                row_str += "@."
            if char == "O":
                row_str += "[]"
        new_map.append(row_str)
    robo_pos = find_robot(new_map)

        # directions x, y
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    # move robo
    for char in input[1]:
        robo_pos = find_robot(new_map)
        if char == ">":
            get_everything_moving(new_map, robo_pos, directions[0])
            target_field = move_target(map, robo_pos, directions[0])
            if target_field:
                map = execute_move(map, robo_pos, target_field, directions[0])
        if char == "v":
            get_everything_moving(new_map, robo_pos, directions[1])
            target_field = move_target(map, robo_pos, directions[1])
            if target_field:
                map = execute_move(map, robo_pos, target_field, directions[1])
        if char == "<":
            get_everything_moving(new_map, robo_pos, directions[2])
            if target_field:
                map = execute_move(map, robo_pos, target_field, directions[2])
        if char == "^":
            get_everything_moving(new_map, robo_pos, directions[3])
            if target_field:
                map = execute_move(map, robo_pos, target_field, directions[3])
    

def get_everything_moving(map: list[str], robo_pos: tuple, direction: tuple):
    no_rows = len(map)
    no_cols = len(map[0])
    i = 1
    queue = [robo_pos]
    moveing_group = []
    while queue:
        new_pos = queue.pop()
        new_pos = new_pos[0] + direction[0], new_pos[1] + direction[1]
        if map[new_pos[1]][new_pos[0]] == "[":
            moveing_group.append(new_pos)
            moveing_group.append((new_pos[0] + 1, new_pos[1]))
            queue.append(new_pos)
            queue.append((new_pos[0] + 1, new_pos[1]))
        if map[new_pos[1]][new_pos[0]] == "]":
            moveing_group.append(new_pos)
            moveing_group.append((new_pos[0] - 1, new_pos[1]))
            queue.append(new_pos)
            queue.append((new_pos[0] - 1, new_pos[1]))
        i += 1
    print("ente")


if __name__ == "__main__":
    input = parse(input_file_path)
    print("total objectiv positions: ", part_one(input))
    print("sum gps coordinates: ", part_two(input))