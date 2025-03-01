input_file_path = "input/day21input.txt"

def parse() -> list[str]:
    input = ""
    with open(input_file_path, "r") as f:
        input = f.read()
    return input.split("\n")

def part_one(input: list[str]) -> int:
    numeric_keypad = {}
    numeric_keypad["0"] = (1, 0)
    numeric_keypad["A"] = (2, 0)
    numeric_keypad["1"] = (0, 1)
    numeric_keypad["2"] = (1, 1)
    numeric_keypad["3"] = (2, 1)
    numeric_keypad["4"] = (0, 2)
    numeric_keypad["5"] = (1, 2)
    numeric_keypad["6"] = (2, 2)
    numeric_keypad["7"] = (0, 3)
    numeric_keypad["8"] = (1, 3)
    numeric_keypad["9"] = (2, 3)

    dir_keypad = {}
    dir_keypad["<"] = (0, 0)
    dir_keypad["v"] = (1, 0)
    dir_keypad[">"] = (2, 0)
    dir_keypad["^"] = (1, 1)
    dir_keypad["A"] = (2, 1)
    total = 0
    for el in input:
        curr_field = "A"
        path = ""
        poss_moves = []
        # control num pad
        for char in el:
            poss_moves.append(breadth_first_search(numeric_keypad, curr_field, char))
            #poss_moves.append(get_instruction(numeric_keypad, curr_field, char))
            curr_field = char
        poss_moves = create_str_combinations(poss_moves)
        # control robo 1
        curr_field = "A"
        new_paths = []
        for path in poss_moves:
            new_poss = []
            for char in path:
                new_poss.append(get_instruction(dir_keypad, curr_field, char))
                curr_field = char
            new_paths.extend(create_str_combinations(new_poss))
        # control robo 2
        new_path2 = []
        curr_field = "A"
        for new_path in new_paths:
            new_poss = []
            for char in new_path:
                new_poss.append(get_instruction(dir_keypad, curr_field, char))
                curr_field = char
            new_path2.extend(create_str_combinations(new_poss))
        new_path2.sort(key=lambda el: len(el))
        len_str = len(new_path2[0])
        input_as_int = int(el[:-1])
        total += len_str * input_as_int
    return(total)

def get_instruction(pad, start: str, end: str) -> list[str]:
    dir_symbols = [">", "v", "<", "^"]

    diff = (pad[start][0] - pad[end][0], 
            pad[start][1] - pad[end][1])

    move_str = ""
    move_str1 = ""
    move_str2 = ""
    # if len(pad) == 5:
    #     # left
    #     if diff[0] > 0: 
    #         move_str += diff[0] * dir_symbols[2]
    #     else:
    #     # right
    #         move_str +=  abs(diff[0]) * dir_symbols[0]
    #     if diff[1] < 0:
    #     # top
    #         return [move_str + abs(diff[1]) * dir_symbols[3] + "A"]
    #     else:
    #     # bot
    #         return [diff[1] * dir_symbols[1] + move_str + "A"]

    # left
    if diff[0] > 0: 
        move_str += diff[0] * dir_symbols[2]
    else:
    # right
        move_str +=  abs(diff[0]) * dir_symbols[0]
    
    # top
    if diff[1] < 0:
        move_str1 = abs(diff[1]) * dir_symbols[3] + move_str
        # if not start on row 0 and end on col 0
        if not (pad[start][1] == 0 and pad[end][0] == 0):
            move_str2 = move_str + abs(diff[1]) * dir_symbols[3]
    else:
    # bot
        move_str1 = move_str + diff[1] * dir_symbols[1]
        # if not start on col 0 and end on row 0
        if not (pad[start][0] == 0 and pad[end][0] == 0):
            move_str2 = move_str + abs(diff[1]) * dir_symbols[1]
    move_str1 += "A"
    move_str2 = move_str2 + "A" if move_str2 else ""
    moves = [move_str1, move_str2] if move_str2 and move_str1 != move_str2 else [move_str1]

    return moves

def create_str_combinations(poss_moves: list[list[str]]) -> list[str]:
    combined_moves = []
    while len(poss_moves) >= 2:
        moves = poss_moves.pop(0)
        moves2 = poss_moves.pop(0)
        combined_moves = []
        for move in moves:
            for move2 in moves2:
                combined_moves.append(move + move2)
        poss_moves.insert(0, combined_moves)
    return combined_moves

def breadth_first_search(keypad, start: tuple, end: tuple):
    start = keypad[start]
    end = keypad[end]
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    dir_symbols = [">", "^", "<", "v"]
    visited_fields = []
    queue = [(start, "")]
    routes = []

    while queue:
        field, move_str = queue.pop(0)

        visited_fields.append(field)

        if field == end:
            routes.append(move_str + "A")


        for i, direction in enumerate(directions):
            new_el = field[0] + direction[0], field[1] + direction[1]
            
            if new_el[0] < 3 and new_el[1] < 4 and new_el != (0, 0)  and new_el[0] >= 0 and new_el[1] >= 0 and new_el not in visited_fields:
                queue.append((new_el, move_str + dir_symbols[i]))
    
    return routes

if __name__ == "__main__":
    input = parse()
    print("part one: ", part_one(input))