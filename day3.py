import re
input_file_path = "day3input.txt"

def part_one():
    with open(input_file_path, "r") as f:
        text = f.read()
        matches = re.findall(r"mul\([0-9]+,[0-9]+\)", text)
        total = 0
        for match in matches:
            substr = match[4:-1]
            left, right = substr.split(",")
            total += int(left) * int(right)
        print("total: ", total)

def part_two():
    text = ""
    with open(input_file_path, "r") as f:
        text = f.read()
    matches = re.findall(r"mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)", text)

    total = 0
    multiply = True
    for match in matches:
        if match == "do()":
            multiply = True
        elif match == "don't()":
            multiply = False
        else:
            if multiply:
                substr = match[4:-1]
                left, right = substr.split(",")
                total += int(left) * int(right)
    print("total: ", total)

if __name__ == "__main__":
    part_one()
    part_two()