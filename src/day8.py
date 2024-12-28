import math

def part_one(antennas: dict[str:list]) -> int:
    antennas, no_of = antennas
    no_of_cols, no_of_rows = no_of
    anti_nodes = set()
    for antenna_type, pos_list in antennas.items():
        for antenna in pos_list:
            for other_antenna in pos_list:
                if antenna != other_antenna:
                    anti_nodes = anti_nodes.union(create_anti_nodes(antenna, other_antenna))

    result = 0
    for anti_node in anti_nodes:
        if anti_node[0] >= 0 and anti_node[0] < no_of_cols and \
            anti_node[1] >= 0 and anti_node[1] < no_of_rows:
            result += 1
    return result

def part_two(antennas: dict[str:list]) -> int:
    antennas, no_of = antennas
    no_of_cols, no_of_rows = no_of
    anti_nodes = set()
    for antenna_type, pos_list in antennas.items():
        for antenna in pos_list:
            for other_antenna in pos_list:
                if antenna != other_antenna:
                    anti_nodes = anti_nodes.union(create_anti_nodes2(antenna, other_antenna, no_of_cols, no_of_rows))

    return len(anti_nodes)

def get_file_content(file_path_str) -> str:
    input = ""
    with open(file_path_str, "r") as f:
        input = f.read()
    return input

def parse(input: list[str]) -> tuple[dict[str,list], tuple[int,int]]:
    antennas = dict()
    input = input.split("\n")
    no_of_rows = len(input)
    no_of_cols = len(input[0])

    for y, line in enumerate(input):
        for x, char in enumerate(line):
            if char != ".":
                if val := antennas.get(char):
                    val.append((x, y))
                else:
                    antennas[char] = [(x, y)]
    return antennas, (no_of_cols, no_of_rows)

def create_anti_nodes(pt1: tuple, pt2: tuple) -> set:
    diff_x = pt1[0] - pt2[0]
    diff_y = pt1[1] - pt2[1]
    anti_nodes = set()
    anti_node1 = (pt1[0] + diff_x, pt1[1] + diff_y)
    anti_node2 = (pt2[0] + diff_x, pt2[1] + diff_y)

    if anti_node1 == pt1 or anti_node1 == pt2:
        anti_nodes = anti_nodes.union({(pt1[0] + diff_x * -1, pt1[1] + diff_y * -1)})
    else:
        anti_nodes = anti_nodes.union({anti_node1})

    if anti_node2 == pt1 or anti_node2 == pt2:
        anti_nodes = anti_nodes.union({(pt2[0] + diff_x * -1, pt2[1] + diff_y * -1)})
    else:
        anti_nodes = anti_nodes.union({anti_node2})
    return anti_nodes

def create_anti_nodes2(pt1: tuple, pt2: tuple, no_of_cols: int, no_of_rows: int) -> set:
    diff_x = pt1[0] - pt2[0]
    diff_y = pt1[1] - pt2[1]
    anti_nodes = set()
    times_x = math.floor((abs(diff_x) + pt1[0]) / no_of_cols)
    times_y = math.floor((abs(diff_y) + pt1[1]) / no_of_rows)
    times = min(times_x, times_y)
    i = -times

    while True:
        anti_node1 = (pt1[0] + diff_x * i, pt1[1] + diff_y * i)
        if anti_node1[0] < 0 or anti_node1[0] >= no_of_cols \
            or anti_node1[1] < 0 or anti_node1[1] >= no_of_rows:
            break
        anti_nodes = anti_nodes.union({anti_node1})
        i += 1

    return anti_nodes


if __name__ == "__main__":
    input_file_path = "input/day8input.txt"
    input = get_file_content(input_file_path)
    input = parse(input)
    print("part one: ", part_one(input))
    print("part two: ", part_two(input))