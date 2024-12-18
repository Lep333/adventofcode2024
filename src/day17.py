import copy
import sys

def parse(input: str) -> tuple:
    regs, program = input.split("\n\n")
    reg0, reg1, reg2 = regs.split("\n")
    _, _, reg0 = reg0.split()
    _, _, reg1 = reg1.split()
    _, _, reg2 = reg2.split()
    reg0 = int(reg0)
    reg1 = int(reg0)
    reg2 = int(reg0)

    _, program = program.split()
    program = program.split(",")
    return reg0, reg1, reg2, program

def part_one(input: tuple) -> str:
    output = []
    reg0, reg1, reg2, program = input
    instruction_pointer = 0

    while instruction_pointer < len(program):
        if program[instruction_pointer] == "0":
            result = int(reg0 / 2 ** combo_code(program[instruction_pointer + 1], reg0, reg1, reg2))
            reg0 = result
        if program[instruction_pointer] == "1":
            reg1 = reg1 ^ int(program[instruction_pointer + 1])
        if program[instruction_pointer] == "2":
            reg1 = combo_code(program[instruction_pointer + 1], reg0, reg1, reg2) % 8
        if program[instruction_pointer] == "3":
            if reg0:
                instruction_pointer = int(program[instruction_pointer + 1])
                continue
        if program[instruction_pointer] == "4":
            reg1 = reg1 ^ reg2
        if program[instruction_pointer] == "5":
            out = combo_code(program[instruction_pointer + 1], reg0, reg1, reg2) % 8
            output.append(str(out))
        if program[instruction_pointer] == "6":
            result = int(reg0 / 2 ** combo_code(program[instruction_pointer + 1], reg0, reg1, reg2))
            reg1 = result
        if program[instruction_pointer] == "7":
            result = int(reg0 / 2 ** combo_code(program[instruction_pointer + 1], reg0, reg1, reg2))
            reg2 = result
        instruction_pointer += 2
    return ",".join(output)

def part_two(input: tuple, index = 0) -> int:
    reg0, reg1, reg2, program = input
    program_as_str = "".join(program)
    intern_index = len(program_as_str) - index - 1
    if not index:
        index = 0   
        reg0 = 8 ** intern_index
    
    for _ in range(8):
        result = part_one((reg0, copy.copy(reg1), copy.copy(reg2), copy.copy(program)))
        result = "".join(result.split(","))
        
        if result[intern_index] == program_as_str[intern_index]:
            if index == len(program_as_str) - 1:
                return reg0
            res = part_two((reg0, copy.copy(reg1), copy.copy(reg2), copy.copy(program)), index + 1)
            if res:
                return res
        reg0 +=  8 ** intern_index
    return None


def combo_code(combo_operand: str, reg_a: int, reg_b: int, reg_c: int):
    combo_operand = int(combo_operand)
    if combo_operand >= 0 and combo_operand <= 3:
        return combo_operand
    if combo_operand == 4:
        return reg_a
    if combo_operand == 5:
        return reg_b
    if combo_operand == 6:
        return reg_c

if __name__ == "__main__":
    input_file_path = "input/day17input.txt"
    input = ""
    with open(input_file_path, "r") as f:
        input = f.read()
    input = parse(input)
    print("result part one: ", part_one(copy.deepcopy(input)))
    print("result part two: ", part_two(copy.deepcopy(input)))