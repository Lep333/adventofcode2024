input_file_path = "day5input.txt"

def part_one():
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
