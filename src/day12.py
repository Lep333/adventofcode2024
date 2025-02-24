input_file_path = "input/day12input.txt"

def parse() -> list[str]:
    with open(input_file_path, "r") as f:
        return f.read().split()

def part_one(input: list[str]) -> int:
    visited_fields = []

    row_count = len(input)
    col_count = len(input[0])
    curr_area_queue = []
    curr_plant = ""
    fence_length = 0
    area_size = 0
    total_cost = 0
    visited_fields_current_field = []
    neighbours_directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    regions = 0

    for y, row in enumerate(input):
        for x, plant in enumerate(row):
            if (y, x) in visited_fields:
                continue
            curr_area_queue.append((y, x))
            curr_plant = plant
            regions += 1
            while curr_area_queue:
                area = curr_area_queue.pop(0)
                if area in visited_fields_current_field:
                    continue
                if area[0] < 0 or area[1] < 0 or area[0] >= row_count or \
                    area[1] >= col_count or input[area[0]][area[1]] != curr_plant:
                    fence_length += 1
                else:
                    for direction in neighbours_directions:
                        new_area = (area[0] + direction[0], area[1] + direction[1])
                        curr_area_queue.append(new_area)
                    visited_fields_current_field.append(area)
                    area_size += 1
                    visited_fields.append(area)
            total_cost += area_size * fence_length
            area_size = 0
            fence_length = 0
            visited_fields_current_field = []
    return total_cost

def part_two(input: list[list[str]]) -> int:
    total = 0
    visited_fields = []
    local_fields = []
    for y, line in enumerate(input):
        for x, plant in enumerate(line):
            if (x, y) in visited_fields:
                continue
            fences, local_fields = get_fences_and_fields(input, (x, y))
            fences = get_connected_fences(fences)
            total += len(fences) * len(local_fields)
            visited_fields.extend(local_fields)
            local_fields = []
    return total

def get_fences_and_fields(input: list[list[str]], start: tuple) -> tuple:
    line_nos = len(input[0])
    row_nos = len(input)
    fences = [] 
    local_fields = []
    queue = [start]
    neighbours_directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    
    while queue:
        field = queue.pop(0)
        if field in local_fields:
            continue
        local_fields.append(field)
        # check neighbours
        for fence_type, direction in enumerate(neighbours_directions):
            if not out_of_bounds(input, field[0] + direction[0], field[1] + direction[1]) \
                and input[field[1] + direction[1]][field[0] + direction[0]] == input[field[1]][field[0]]:
                queue.append((field[0] + direction[0], field[1] + direction[1]))
            else:
                fences.append([(field[0], field[1], fence_type)])
    return fences, local_fields

def get_connected_fences(fences: list[list[tuple]]) -> list[list[tuple]]:
    for i in range(len(fences)):
        fence_is_subset = False
        fence = fences.pop(0)
        for fence_og_el in fence:
            if fence_is_subset:
                break
            left_neighbour = (fence_og_el[0] - 1, fence_og_el[1], fence_og_el[2])
            top_neighbour = (fence_og_el[0], fence_og_el[1] - 1, fence_og_el[2])
            right_neighbour = (fence_og_el[0] + 1, fence_og_el[1], fence_og_el[2])
            bottom_neighbour = (fence_og_el[0], fence_og_el[1] + 1, fence_og_el[2])
            neighbour1 =  left_neighbour if fence_og_el[2] % 2 == 0 else top_neighbour
            neighbour2 =  right_neighbour if fence_og_el[2] % 2 == 0 else bottom_neighbour
            for straight_fence in fences:
                if neighbour1 in straight_fence or neighbour2 in straight_fence:
                    straight_fence.extend(fence)
                    fence_is_subset = True
                    break
        if not fence_is_subset:
            fences.append(fence)
    return fences

def out_of_bounds(input: list[str], x: int, y: int) -> bool:
    no_of_cols = len(input[0])
    no_of_rows = len(input)

    if x < 0 or x >= no_of_cols or y < 0 or y >= no_of_rows:
        return True
    return False

if __name__ == "__main__":
    input = parse()
    print("fence costs: ", part_one(input))
    input = parse()
    print("fence costs: ", part_two(input))