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
    print("found regions: ", regions)
    print("no visited fields: ", len(visited_fields))
    return total_cost

def part_two(input: list[str]):
    total_cost = 0
    visited_fields = []
    regions = 0

    for y, row in enumerate(input):
        for x, char in enumerate(row):
            if (x, y) in visited_fields:
                continue
            fences, vis_fields = group_fences(input, (x, y))
            visited_fields.extend(vis_fields)
            regions += 1
            for key, fences_ in fences.items():
                combined_fences = []
                for fence in fences_:
                    one = (fence[0] -1, fence[1], fence[2]) if fence[2] == 0 else (fence[0], fence[1] -1, fence[2])
                    two = (fence[0] +1, fence[1], fence[2]) if fence[2] == 0 else (fence[0], fence[1] +1, fence[2])
                    for c_fence in combined_fences:
                        if one in c_fence or two in c_fence:
                            c_fence.append(fence)
                            break
                    else:
                        combined_fences.append([fence])
                total_cost += len(combined_fences) * len(vis_fields)

    print("regions found: ", regions)
    print("no visited fields: ", len(visited_fields))
    return total_cost

def group_fences(input: list[str], start: tuple[int]) -> dict[list]:
    # horizontal = 0
    # vertical = 1
    fences = dict()
    queue = [start]
    neighbours_directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited_fields = [start]

    while queue:
        x, y = queue.pop(0)
    # for y, row in enumerate(input):
    #     for x, char in enumerate(row):
    #         curr_plant = input[y][x]
        curr_plant = input[y][x]

        for direction in neighbours_directions:
            new_x = x + direction[0]
            new_y = y + direction[1]
            if (not out_of_bounds(input, new_x, new_y)) and input[new_y][new_x] == curr_plant and (new_x, new_y) not in visited_fields:
                queue.append((new_x, new_y))
                visited_fields.append((new_x, new_y))
        
        if not fences.get(curr_plant):
            fences[curr_plant] = []

        # top
        if out_of_bounds(input, x, y - 1) or input[y - 1][x] != curr_plant:
            fence_list = fences[curr_plant]
            fence_list.append((x, y, 0))
        # right
        if out_of_bounds(input, x + 1, y) or input[y][x + 1] != curr_plant:
            fence_list = fences[curr_plant]
            fence_list.append((x + 1, y, 1))
        # bottom
        if out_of_bounds(input, x, y + 1) or input[y + 1][x] != curr_plant:
            fence_list = fences[curr_plant]
            fence_list.append((x, y + 1, 0))
        # left
        if out_of_bounds(input, x - 1, y) or input[y][x - 1] != curr_plant:
            fence_list = fences[curr_plant]
            fence_list.append((x, y, 1))

    return fences, visited_fields

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