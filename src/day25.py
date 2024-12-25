def part_one(input: list[list[str]]) -> int:
    locks = [element_to_height(el) for el in input if el[0][0] == "#"]
    keys = [element_to_height(el) for el in input if el[0][0] == "."]

    total = 0
    for lock in locks:
        for key in keys:
            if combination_fits(lock, key):
                total += 1

    return total

def element_to_height(input: list[str]) -> list[int]:
    heights = []
    for x in range(len(input[0])):
        height = 0
        for y in range(1, len(input) - 1):
            if input[y][x] == "#":
                height += 1
        heights.append(height)
    return heights


def combination_fits(lock: list[str], key: list[str]) -> bool:
    for y in range(len(lock)):
        if lock[y] +  key[y] > 5:
            return False
    return True

if __name__ == "__main__":
    input_file_path = "input/day25input.txt"
    input = ""
    with open(input_file_path, "r") as f:
        input = f.read()
    input = input.split("\n\n")
    input = [el.split("\n") for el in input]
    print("part one: ", part_one(input))