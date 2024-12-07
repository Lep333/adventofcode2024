from itertools import product

input_file_path = "day7input.txt"

def part_one():
    with open(input_file_path, "r") as f:
        solution = 0
        for line in f.readlines():
            left_eq, nums = line.split(":")
            nums = nums.split()
            exp = len(nums) - 1
            equation_correct = False
            for i in range(2**exp):
                if equation_correct:
                    break
                total = int(nums[0])
                for m in range(len(nums) - 1):
                    if i & 2**m:
                        total += int(nums[m + 1])
                    else:
                        total *= int(nums[m + 1])
                if int(left_eq) == total:
                    equation_correct = True
                    solution += int(left_eq)
        print(solution)
                
def part_two():
    with open(input_file_path, "r") as f:
        lines = f.readlines()

    solution = 0
    for line in lines:
        left_eq, nums = line.split(":")
        nums = nums.split()
        exp = len(nums) - 1
        equation_correct = False
        
        for combination in product([0,1,2], repeat=len(nums) - 1):
            total = int(nums[0])
            if equation_correct:
                break
            for i, val in enumerate(combination):
                
                if val == 0:
                    total += int(nums[i + 1])
                elif val == 1:
                    total *= int(nums[i + 1])
                elif val == 2:
                    total = int(str(total) + nums[i + 1])
            if total == int(left_eq):
                equation_correct = True
                solution += int(left_eq)
    print(solution)

if __name__ == "__main__":
    part_one()
    part_two()