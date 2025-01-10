import itertools
import copy

def part_one(input: str) -> int:
    var_init, ops = input.split("\n\n")
    var_init = var_init.split("\n")
    ops = ops.split("\n")
    vars = {get_key(var): int(get_val(var)) for var in var_init}
    ops = [el.replace("->", "").split() for el in ops]
    return compute(vars, ops)

def part_two(input: str) -> str:
    var_init, ops = input.split("\n\n")
    var_init = var_init.split("\n")
    ops = ops.split("\n")
    vars = {get_key(var): int(get_val(var)) for var in var_init}
    ops = [el.replace("->", "").split() for el in ops]

    i = 0
    x_sum = 0
    y = 0
    y_sum = 0
    while True:
        x_str = f"x0{i}" if i < 10 else f"x{i}"
        y_str = f"y0{i}" if i < 10 else f"y{i}"
        if vars.get(x_str) == None and vars.get(y_str) == None:
            break
        if x_val := vars.get(x_str):
            x_sum += x_val * 2 ** i
        if y_val := vars.get(y_str):
            y_sum += y_val * 2 ** i
        i += 1

    i = 0
    for perm in itertools.permutations(range(len(ops)), r=8):
        new_ops = copy.deepcopy(ops)
        new_ops[perm[0]][3], new_ops[perm[1]][3] = new_ops[perm[1]][3], new_ops[perm[0]][3]
        new_ops[perm[2]][3], new_ops[perm[3]][3] = new_ops[perm[3]][3], new_ops[perm[2]][3]
        new_ops[perm[4]][3], new_ops[perm[5]][3] = new_ops[perm[5]][3], new_ops[perm[4]][3]
        new_ops[perm[6]][3], new_ops[perm[7]][3] = new_ops[perm[7]][3], new_ops[perm[6]][3]
        print(i)
        i += 1
        result = compute(vars, new_ops)
        print(bin(result), bin(x_sum + y_sum))
        if result == x_sum + y_sum:
            print("yoever!")
            break

def get_key(line: str) -> str:
    return line.split(": ")[0]

def get_val(line: str) -> str:
    return line.split(": ")[1]

def compute(vars: dict[int], ops: list[list[str]]) -> int:
    queue = ops
    i = 0
    while queue:
        i += 1
        op = queue.pop(0)
        if vars.get(op[0]) != None and vars.get(op[2]) != None:
            if op[1] == "AND":
                vars[op[3]] = vars[op[0]] & vars[op[2]]
            if op[1] == "OR":
                vars[op[3]] = vars[op[0]] | vars[op[2]]
            if op[1] == "XOR":
                vars[op[3]] = vars[op[0]] ^ vars[op[2]]
            i = 0
        else:
            queue.append(op)
        if i == len(queue):
            break
    
    output = ""
    for i in range(len(vars)):
        z_str = ""
        if i < 10:
            z_str = f"z0{i}"
        else:
            z_str = f"z{i}"
        if vars.get(z_str) != None:
            output = str(vars[z_str]) + output
        else:
            break
    return int(output, 2)

if __name__ == "__main__":
    input_file_path = "input/day24input.txt"
    input = ""
    with open(input_file_path, "r") as f:
        input = f.read()
    print("part one: ", part_one(input))
    print("part two: ", part_two(input))
            