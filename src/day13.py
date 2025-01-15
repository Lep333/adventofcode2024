input_file_path="input/day13input.txt"

def parse(position_offset: int = 0) -> list[tuple]:
    text = ""
    with open(input_file_path, "r") as f:
        text = f.read()
    
    text = text.replace("X", "")
    text = text.replace("Y", "")
    text = text.replace("=", "")
    text = text.replace(",", "")
    text = text.replace("\n\n", "\n")
    text = text.split("\n")

    button_a = ()
    button_b = ()
    prize = ()
    bandits = []
    for i, row in enumerate(text):
        if not row:
            continue
        if i % 3 == 0:
            _, _, x, y = row.split()
            button_a = int(x), int(y)
        elif i % 3 == 1:
            _, _, x, y = row.split()
            button_b = int(x), int(y)
        else:
            _, x, y = row.split()
            prize = int(x) + position_offset, int(y) + position_offset
            bandits.append((button_a, button_b, prize))
            button_a = ()
            button_b = ()
            prize = ()
    return bandits

def part_one(bandits: list[tuple]) -> int:
    total_cost = 0
    for bandit in bandits:
        total_cost += gaussian_elim(bandit)

    return total_cost

def part_two(bandits: list[tuple]) -> int:
    a_costs = 3
    b_costs = 1

    total_cost = 0
    for bandit in bandits:
        total_cost += gaussian_elim(bandit)

    return int(total_cost)

def gaussian_elim(bandit: list) -> int:
    a_costs = 3
    b_costs = 1
    cost = 0

    x = [bandit[0][0], bandit[1][0], bandit[2][0]]
    y = [bandit[0][1], bandit[1][1], bandit[2][1]]
    factor = y[0] / x[0]
    y[0] = y[0] - x[0] * factor
    y[1] = y[1] - x[1] * factor
    y[2] = y[2] - x[2] * factor
    y_sol = y[2] / y[1]
    x_sol = (x[2] - x[1] * y_sol) / x[0]
    x_f = abs(round(x_sol, 0) - x_sol) > 0.001
    y_f = abs(round(y_sol, 0) - y_sol) > 0.001
    if not (x_f or y_f):
        cost = round(x_sol, 0) * a_costs + round(y_sol, 0) * b_costs

    return cost

if __name__ == "__main__":
    position_offset = 10000000000000
    input = parse()
    print("total cost: ", part_one(input))
    input = parse(position_offset=position_offset)
    print("total cost: ", part_two(input))