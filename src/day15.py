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
    return calculate_result(map)

def calculate_result(map: list[str]) -> int:
    # calculate result
    result = 0
    for y, row in enumerate(map):
        for x, char in enumerate(row):
            if char in ["O", "["]:
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
        new_map.append(list(row_str))
    robo_pos = find_robot(new_map)

    # directions x, y
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    # move robo
    for char in input[1]:
        robo_pos = find_robot(new_map)
        if char == ">":
            move_horizontal(new_map, robo_pos, directions[0])
        if char == "v":
            move_vertical(new_map, robo_pos, directions[1])
        if char == "<":
            move_horizontal(new_map, robo_pos, directions[2])
        if char == "^":
            move_vertical(new_map, robo_pos, directions[3])
    
    return calculate_result(new_map)

def move_horizontal(map: list[str], robo_pos: tuple, direction: tuple):
    new_pos = (robo_pos[0] + direction[0], robo_pos[1] + direction[1])
    i = 0
    while map[new_pos[1]][new_pos[0]] not in ["#", "."]:
        new_pos = (new_pos[0] + direction[0], new_pos[1] + direction[1])
        i += 1
    if map[new_pos[1]][new_pos[0]] == ".":
        switch_pos = new_pos[0] - direction[0], new_pos[1] - direction[1]
        for _ in range(i + 1):
            temp = map[switch_pos[1]][switch_pos[0]]
            map[switch_pos[1]][switch_pos[0]] = map[new_pos[1]][new_pos[0]]
            map[new_pos[1]][new_pos[0]] = temp
            new_pos = switch_pos
            switch_pos = switch_pos[0] - direction[0], switch_pos[1] - direction[1]

def move_vertical(map: list[str], robo_pos: tuple, direction: tuple):
    moveing_group = find_fields_to_move(map, robo_pos, direction)
    move_group(map, moveing_group, direction)

def find_fields_to_move(map: list[str], robo_pos: tuple, direction: tuple) -> list:
    move_group = []
    queue = [robo_pos]
    visited_fields = []
    while queue:
        pos = queue.pop(0)
        
        if map[pos[1]][pos[0]] == "." or pos in visited_fields:
            continue
        visited_fields.append(pos)
        move_group.append(pos)

        # check if in move direction boxes
        new_pos = pos[0] + direction[0], pos[1] + direction[1]
        if map[new_pos[1]][new_pos[0]] == "[":
            # add right part of box
            pos_box_right_part = new_pos[0] + 1, new_pos[1]
            queue.append(pos_box_right_part)
        if map[new_pos[1]][new_pos[0]] == "]":
            # add left part of box
            pos_box_left_part = new_pos[0] - 1, new_pos[1]
            queue.append(pos_box_left_part)
        # collision detection
        if map[new_pos[1]][new_pos[0]] == "#":
            return
        queue.append(new_pos)
    return move_group

def move_group(map: list[str], move_group: list, direction: tuple):
    while move_group:
        pos1 = move_group.pop()
        swap_pos = pos1[0] + direction[0], pos1[1] + direction[1]
        temp = map[swap_pos[1]][swap_pos[0]]
        map[swap_pos[1]][swap_pos[0]] = map[pos1[1]][pos1[0]]
        map[pos1[1]][pos1[0]] = temp

if __name__ == "__main__":
    input = parse(input_file_path)
    print("total objectiv positions: ", part_one(input))
    print("sum gps coordinates: ", part_two(input))