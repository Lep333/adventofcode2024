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
    for y, row in enumerate(input):
        for x, plant in enumerate(row):
            if (y, x) in visited_fields:
                continue
            curr_area_queue.append((y, x))
            curr_plant = plant
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

def part_two(input: list[str]):
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
    curr_border = []
    for y, row in enumerate(input):
        for x, plant in enumerate(row):
            if (y, x) in visited_fields:
                continue
            curr_area_queue.append((y, x))
            curr_plant = plant
            while curr_area_queue:
                area = curr_area_queue.pop(0)
                if area in visited_fields_current_field:
                    continue
                if area[0] < 0 or area[1] < 0 or area[0] >= row_count or \
                    area[1] >= col_count or input[area[0]][area[1]] != curr_plant:
                    fence_length += 1
                    curr_border.append(area)
                else:
                    for direction in neighbours_directions:
                        new_area = (area[0] + direction[0], area[1] + direction[1])
                        curr_area_queue.append(new_area)
                    visited_fields_current_field.append(area)
                    area_size += 1
                    visited_fields.append(area)
            sides = 0
            curr_side = []
            queue = []
            visited_borders = []
            sides = []
            for border in curr_border:
                queue = [border]
                curr_side = [border]
                while queue:
                    border = queue.pop()
                    if border in visited_borders:
                        continue
                    for other_border in curr_border:
                        if border == other_border:
                            continue
                        if other_border in curr_side:
                            continue
                        for direction in neighbours_directions:
                            if border[0] == other_border[0] + direction[0] and border[1] == other_border[1] + direction[1]:
                                queue.append(other_border)
                                curr_side.append(other_border)
                                visited_borders.append(border)
                sides.append(curr_side)
                        
            total_cost += area_size * fence_length
            area_size = 0
            fence_length = 0
            visited_fields_current_field = []
    return total_cost

if __name__ == "__main__":
    input = parse()
    print("fence costs: ", part_one(input))
    input = parse()
    print("fence costs: ", part_two(input))