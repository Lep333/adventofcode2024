input_file_path = "day5input.txt"

def part_one():
    text = ""
    
    with open(input_file_path, "r") as f:
        text = f.read()

<<<<<<< HEAD
    no_of_cols = len(text.split("\n")[0])
    no_of_rows = len(text.split("\n"))
    rows = text.split("\n")

    start_row = 0
    start_col = 0
    found_start = False
    for y, row in enumerate(rows):
        for x, col in enumerate(row):
            if col == "^":
                found_start = True
                start_row = y
                start_col = x
                break
        if found_start:
            break
    
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    field = text.split("\n")
    curr_direction = 0 # (y, x)
    moved_fields = 0
    next_field = (y, x)
    visited_fields = {next_field}

    while True:
        next_y = next_field[0] + directions[curr_direction][0]
        next_x = next_field[1] + directions[curr_direction][1]
        if next_y < 0 or next_x < 0 or next_y >= no_of_rows or next_x >= no_of_cols:
            break
        if field[next_y][next_x] == "#":
            curr_direction += 1
            curr_direction %= 4
        else:
            next_field = (next_y, next_x)
            visited_fields = visited_fields.union({next_field})
            moved_fields += 1
    print(len(visited_fields))

if __name__ == "__main__":
    part_one()
=======
    order_rules, orders = text.split("\n\n")
    order_rules = order_rules.split("\n")

    rule_book = {}
    for order_rule in order_rules:
        before, after = order_rule.split("|")
        if rule_book.get(after):
            rule_book[after].append(before)
        else:
            rule_book[after] = [before]

    total_middle_page_number = 0

    orders = orders.split("\n")
    for order in orders:
        curr_rules = []
        valid_update = True
        order_pages = order.split(",")
        for order_page in order_pages:
            if order_page in curr_rules:
                valid_update = False
                break
            if rules := rule_book.get(order_page):
                curr_rules.extend(rules)
        if valid_update:
            total_middle_page_number += int(order_pages[int(len(order_pages) / 2)])
    print(total_middle_page_number)

def part_two():
    text = ""
    
    with open(input_file_path, "r") as f:
        text = f.read()

    order_rules, orders = text.split("\n\n")
    order_rules = order_rules.split("\n")

    rule_book = {}
    for order_rule in order_rules:
        before, after = order_rule.split("|")
        if rule_book.get(after):
            rule_book[after].append(before)
        else:
            rule_book[after] = [before]

    total_middle_page_number = 0

    orders = orders.split("\n")
    for order in orders:
        order_pages = order.split(",")
        curr_rules = []
        changed = False
        for i in range(len(order_pages)):
            if rules := rule_book.get(order_pages[i]):
                curr_rules.extend(rules)
            if order_pages[i] in curr_rules:
                order_pages[i - 1], order_pages[i] = order_pages[i], order_pages[i - 1]
                changed = True

        if changed:
            total_middle_page_number += int(order_pages[int(len(order_pages) / 2)])
    print(total_middle_page_number)


if __name__ == "__main__":
    part_one()
    part_two()
>>>>>>> bf0905b (Added day5 part one)
