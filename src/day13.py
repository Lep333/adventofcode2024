input_file_path="input/day13input.txt"

def parse() -> list[tuple]:
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
            prize = int(x), int(y)
            bandits.append((button_a, button_b, prize))
            button_a = ()
            button_b = ()
            prize = ()
    return bandits

def parse_part_two() -> list[tuple]:
    text = ""
    with open(input_file_path, "r") as f:
        text = f.read()
    
    text = text.replace("X", "")
    text = text.replace("Y", "")
    text = text.replace("=", "")
    text = text.replace(",", "")
    text = text.replace("\n\n", "\n")
    text = text.split("\n")

    position_offset = 10000000000000
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
            prize = (int(x) + position_offset, int(y) + position_offset)
            bandits.append((button_a, button_b, prize))
            button_a = ()
            button_b = ()
            prize = ()
    return bandits

def part_one(bandits: list[tuple]) -> int:
    max_button_pushes = 100
    a_costs = 3
    b_costs = 1

    total_cost = 0
    for bandit in bandits:
        lowest_price = None
        for a in range(max_button_pushes + 1):
            for b in range(max_button_pushes + 1):
                if bandit[0][0] * a + bandit[1][0] * b == bandit[2][0] and bandit[0][1] * a + bandit[1][1] * b == bandit[2][1]:
                    price = a * a_costs + b * b_costs
                    if not lowest_price or price < lowest_price:
                        lowest_price = price
        if lowest_price:
            total_cost += lowest_price

    return total_cost

def part_two(bandits: list[tuple]) -> int:
    a_costs = 3
    b_costs = 1

    total_cost = 0
    for bandit in bandits:
        lowest_price = None
        a = bandit[2][0] / bandit[0][0]
        x = bandit[2][1] / bandit[0][1]
        while True:
            still_to_do_x = bandit[2][0] - bandit[0][0] * a
            still_to_do_y = bandit[2][1] - bandit[0][1] * a
            times_b = still_to_do_x / bandit[1][0]
            if type(times_b) == int and times_b * bandit[1][1] == still_to_do_y:
                price = a * a_costs + times_b * b_costs
                if not lowest_price or price < lowest_price:
                    total_cost += lowest_price
            a += 1

    return total_cost

if __name__ == "__main__":
    input = parse()
    print("total cost: ", part_one(input))
    input = parse_part_two()
    print("total cost: ", part_two(input))
        
