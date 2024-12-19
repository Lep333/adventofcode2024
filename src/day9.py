input_file_path = "input/day9input.txt"

def parse() -> str:
    with open(input_file_path, "r") as f:
        return f.read()

def part_one(input: str) -> int:
    new_filesystem = ""

    for id, num in enumerate(input):
        if id % 2 == 0:
            file_str = str(id) * int(num)   
        else:
            file_str = "." * int(num)
        new_filesystem += file_str
    while file_system_ordered(new_filesystem):
        for i in range(0, len(new_filesystem), -1):
            if new_filesystem[i] != ".":
                for n in range(len(new_filesystem)):
                    if new_filesystem[n] == ".":
                        new_filesystem[n] = new_filesystem[i]
                        new_filesystem[i] = "."
    
    checksum = 0
    for i, num in enumerate(new_filesystem):
        checksum += i * int(num)
    return checksum

def file_system_ordered(input: str) -> bool:
    char_found = False
    for i in range(0, len(input), -1):
        if input[i] != ".":
            char_found = True
        if input[i] == "." and char_found:
            return False
    return True


if __name__ == "__main__":
    input = parse()
    print("checksum total: ", part_one(input))