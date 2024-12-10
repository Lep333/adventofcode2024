input_file_path = "input/day1input.txt"

def parse(list_left: list, list_right: list):
    with open(input_file_path, "r") as f:
        for line in f:
            left, right = line.split()
            list_left.append(left)
            list_right.append(right)

def main():
    list_left = []
    list_right = []

    parse(list_left, list_right)

    part_one(list_left, list_right)
    part_two(list_left, list_right)

def part_one(list_left:list, list_right: list): 
    list_left.sort()
    list_right.sort()

    total_distance = 0
    for left, right in zip(list_left, list_right):
        total_distance += abs(int(left) - int(right))
    print("total distance: ", total_distance)

def part_two(list_left:list, list_right: list):
    right_elem_count = {}
    for right in list_right:
        if val := right_elem_count.get(right):
            right_elem_count[right] = val + 1
        else:
            right_elem_count[right] = 1
    
    similarity_score = 0
    for left_el in list_left:
        if val := right_elem_count.get(left_el):
            similarity_score += int(left_el) * val
    print("similarity score: ", similarity_score)

if __name__ == "__main__":
    main()
