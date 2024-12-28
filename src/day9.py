input_file_path = "input/day9input.txt"

def parse() -> str:
    with open(input_file_path, "r") as f:
        return f.read()

def part_one(input: str) -> int:
    new_filesystem = create_file_system(input)
    i = len(new_filesystem) - 1
    while i >= 0:
        if new_filesystem[i] != ".":
            for n in range(i):
                if new_filesystem[n] == ".":
                    new_filesystem[n] = new_filesystem[i]
                    new_filesystem[i] = "."
                    break
        i -= 1
    
    return get_checksum(new_filesystem)

def part_two(input: str) -> int:
    new_filesystem = create_file_system(input)
    i = len(new_filesystem) - 1
    start_pos = len(new_filesystem) - 1
    while i > 0:
        if new_filesystem[i] != ".":
            if new_filesystem[i] != new_filesystem[start_pos]:
                start_pos = i
            if start_pos and new_filesystem[start_pos] != new_filesystem[i - 1]:
                space_needed = start_pos - i + 1
                start = space_start_index(new_filesystem, i, space_needed)
                if start >= 0:
                    move_file(new_filesystem, i, start, space_needed)
                start_pos = start_pos - 1
        i -= 1
    
    return get_checksum(new_filesystem)

def create_file_system(input: str) -> list:
    new_filesystem = []

    for id, num in enumerate(input):
        if id % 2 == 0: 
            for i in range(int(num)):
                new_filesystem.append(int(int(id) / 2)) 
        else:
            for i in range(int(num)):
                new_filesystem.append(".")
    return new_filesystem

def space_start_index(filesystem: list, end_index: int, space_needed: int) -> int:
    start = 0
    curr_space_seg = False
    for i, el in enumerate(filesystem):
        if i == end_index:
            break
        if el == "." and not curr_space_seg:
            start = i
            curr_space_seg = True
        if el != ".":
            curr_space_seg = False
        if i - start + 1 >= space_needed and curr_space_seg:
            return start
    return -1

def move_file(filesystem: list, start_file: int, start_space: int, length: int):
    file_id = filesystem[start_file]
    for i in range(length):
        filesystem[start_space + i] = file_id
        filesystem[start_file + i] = "."

def get_checksum(filesystem: list):
    checksum = 0
    for i, num in enumerate(filesystem):
        if num == ".":
            continue
        checksum += i * int(num)
    return checksum

if __name__ == "__main__":
    input = parse()
    print("part one: ", part_one(input))
    print("part two: ", part_two(input))