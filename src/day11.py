input_file_path = "input/day11input.txt"

def parse() -> list[str]:
    with open(input_file_path, "r") as f:
        return f.read().split()

def part_one(input: list[str]) -> int:
    n_blinking = 25
    for i in range(n_blinking):
        m = 0
        while m < len(input):
            if input[m] == "0":
                input[m] = "1"
            elif len(input[m]) % 2 == 0:
                split_index = int(len(input[m]) / 2)
                el = input[m]
                input[m] = str(int(el[split_index:]))
                input.insert(m, str(int(el[0:split_index])))
                m += 1
            else:
                input[m] = str(int(input[m]) * 2024)
            m += 1
    
    return len(input)

def part_two(input: dict) -> int:
    new = dict()
    for el in input:
        if new.get(el):
            new[el] += 1
        else:
            new[el] = 1
    input = new
    n_blinking = 75
    for i in range(n_blinking):
        next_iter = dict()
        keys = input.keys()
        for key in keys:
            if key == "0":
                if next_iter.get("1"):   
                    next_iter["1"] += input[key]
                else: next_iter["1"] = input[key]
            elif len(key) % 2 == 0:
                split_index = int(len(key) / 2)
                el = key
                res1 = str(int(el[split_index:]))
                res2 = str(int(el[0:split_index]))
                if next_iter.get(res1):
                    next_iter[res1] += input[key]
                else: next_iter[res1] = input[key]
                if next_iter.get(res2):
                    next_iter[res2] += input[key]
                else: next_iter[res2] = input[key]
            else:
                el = input[key]
                result = str(int(key) * 2024)
                if next_iter.get(result):
                    next_iter[result] += input[key]
                else: next_iter[result] = input[key]
        input = next_iter
    
    sum = 0
    for key, item in next_iter.items():
        sum += item
    return sum

if __name__ == "__main__":
    input = parse()
    print("sum stones after 25times blinking: ", part_one(input))
    input = parse()
    print("sum stones after 75times blinking: ", part_two(input))