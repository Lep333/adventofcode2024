input_file_path = "day4input.txt"

def part_one():
    text = ""
    with open(input_file_path, "r") as f:
        text = f.readlines()
    
    xmas_count = 0

    for line_no, line in enumerate(text):
        for pos, char in enumerate(line):
            if char == "X":
                # check horizontal
                if len(line) > pos + 3 and line[pos + 1] == "M" and line[pos + 2] == "A" and line[pos + 3] == "S":
                    xmas_count += 1
                # check backwards
                if pos >= 3 and line[pos - 1] == "M" and line[pos - 2] == "A" and line[pos - 3] == "S":
                    xmas_count += 1
                # check vertical
                if len(text) > line_no + 3 and text[line_no + 1][pos] == "M" and text[line_no + 2][pos] == "A" and text[line_no + 3][pos] == "S":
                    xmas_count += 1
                # check vertical backwards
                if line_no >= 3 and text[line_no - 1][pos] == "M" and text[line_no - 2][pos] == "A" and text[line_no - 3][pos] == "S":
                    xmas_count += 1
                # check diagonal right
                if len(text) > line_no + 3 and len(line) > pos + 3 and text[line_no + 1][pos + 1] == "M" and text[line_no + 2][pos + 2] == "A" and text[line_no + 3][pos + 3] == "S":
                    xmas_count += 1
                # check diagonal left
                if len(text) > line_no + 3 and pos >= 3 and text[line_no + 1][pos - 1] == "M" and text[line_no + 2][pos - 2] == "A" and text[line_no + 3][pos - 3] == "S":
                    xmas_count += 1
                # check diagonal backwards left
                if line_no >= 3 and pos >= 3 and text[line_no - 1][pos - 1] == "M" and text[line_no - 2][pos - 2] == "A" and text[line_no - 3][pos - 3] == "S":
                    xmas_count += 1
                # check diagonal backwards right
                if line_no >= 3 and len(line) > pos + 3 and text[line_no - 1][pos + 1] == "M" and text[line_no - 2][pos + 2] == "A" and text[line_no - 3][pos + 3] == "S":
                    xmas_count += 1
    print("xmas_count: ", xmas_count)

def part_two():
    text = ""
    with open(input_file_path, "r") as f:
        text = f.readlines()
    
    xmas_count = 0

    for line_no, line in enumerate(text):
        for pos, char in enumerate(line):
            if char == "A" and pos >= 1 and pos < len(line) - 1 and line_no >= 1 and line_no < len(text) - 1:
                if text[line_no - 1][pos - 1] == "M" and text[line_no + 1][pos + 1] == "S":
                    if text[line_no - 1][pos + 1] == "M" and text[line_no + 1][pos - 1] == "S":
                        xmas_count += 1
                    if text[line_no - 1][pos + 1] == "S" and text[line_no + 1][pos - 1] == "M":
                        xmas_count += 1
                elif text[line_no - 1][pos - 1] == "S" and text[line_no + 1][pos + 1] == "M":
                    if text[line_no - 1][pos + 1] == "M" and text[line_no + 1][pos - 1] == "S":
                        xmas_count += 1
                    if text[line_no - 1][pos + 1] == "S" and text[line_no + 1][pos - 1] == "M":
                        xmas_count += 1

    print("xmas_count: ", xmas_count)

if __name__ == "__main__":
    part_one()
    part_two()