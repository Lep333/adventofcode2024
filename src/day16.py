import copy

def parse(file_path: str) -> list[str]:
    text = []
    with open(file_path, "r") as f:
        text = f.read()
    return text.split()

def part_one(input: list[str]) -> int:
    no_rows = len(input)
    no_cols = len(input[0])
    starting_point = get_starting_point(input)
    # direction 0 = east, 1 = south, 2 = west, 3 = north
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    # queue contains point(x,y), faceing direction, score
    queue = [(starting_point, 0, 0)]
    move_cost = 1
    turn_cost = 1000

    visited_locations = []
    while queue:
        curr_location, direction, score = queue.pop(0)

        if input[curr_location[1]][curr_location[0]] == "E":
            return score
        
        # try move
        new_position = curr_location[0] + directions[direction][0], curr_location[1] + directions[direction][1]
        if not new_position in visited_locations and new_position[0] >= 0 and new_position[0] < no_cols and new_position[1] >= 0 and new_position[1] < no_rows and input[new_position[1]][new_position[0]] != "#":
            new_score = score + move_cost
            queue.append((new_position, direction, new_score))
        
        # turn
        if not curr_location in visited_locations:
            queue.append((curr_location, (direction + 1) % 4, score + turn_cost))
            queue.append((curr_location, (direction + 2) % 4, score + 2 * turn_cost))
            queue.append((curr_location, (direction - 1) % 4, score + turn_cost))
            visited_locations.append(curr_location)
        queue.sort(key=lambda x: x[2])

def part_two(input: list[str]) -> int:
    no_rows = len(input)
    no_cols = len(input[0])
    starting_point = get_starting_point(input)
    # direction 0 = east, 1 = south, 2 = west, 3 = north
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    # queue contains point(x,y), faceing direction, score, path history
    queue = [(starting_point, 0, 0, [starting_point])]
    move_cost = 1
    turn_cost = 1000
    lowest_cost = None

    shortest_paths = set()
    visited_locations = []
    while queue:
        curr_location, direction, score, history = queue.pop(0)

        if lowest_cost and score > lowest_cost:
            break

        if input[curr_location[1]][curr_location[0]] == "E":
            lowest_cost = score
            shortest_paths = shortest_paths.union(set(history))
        
        # try move
        new_position = curr_location[0] + directions[direction][0], curr_location[1] + directions[direction][1]
        if not new_position in visited_locations and new_position[0] >= 0 and new_position[0] < no_cols and new_position[1] >= 0 and new_position[1] < no_rows and input[new_position[1]][new_position[0]] != "#":
            new_score = score + move_cost
            new_history = copy.copy(history)
            new_history.append(new_position)
            queue.append((new_position, direction, new_score, new_history))
        elif new_position in visited_locations and new_position[0] >= 0 and new_position[0] < no_cols and new_position[1] >= 0 and new_position[1] < no_rows and input[new_position[1]][new_position[0]] != "#":
            new_score = score + move_cost
            for i, el in enumerate(queue):
                if el[0] == new_position and direction == el[1] and new_score == el[2]:
                    queue.pop(i)
                    history.extend(el[3])
                    queue.append((el[0], el[1], el[2], history))
                    break
        
        # turn
        if not curr_location in visited_locations:
            queue.append((curr_location, (direction + 1) % 4, score + turn_cost, copy.copy(history)))
            queue.append((curr_location, (direction + 2) % 4, score + 2 * turn_cost, copy.copy(history)))
            queue.append((curr_location, (direction - 1) % 4, score + turn_cost, copy.copy(history)))
            visited_locations.append(curr_location)
        queue.sort(key=lambda x: x[2])
    return len(shortest_paths)
    

def get_starting_point(input: list[str]) -> tuple[tuple]:
    starting_point = ()
    end_point = ()

    for y, row in enumerate(input):
        for x, col in enumerate(row):
            if col == "S":
                starting_point = x, y
            if col == "E":
                end_point = x, y
    
    return starting_point, end_point

if __name__ == "__main__":
    input_file_path = "input/day16input.txt"
    input = parse(input_file_path)
    result_part_one = part_one(input)
    print("lowest score: ", result_part_one)
    result_part_two = part_two(input)
    print("tiles used: ", result_part_two)