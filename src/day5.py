input_file_path = "input/day5input.txt"

def parse() -> str:
    with open(input_file_path, "r") as f:
        return f.read()
    
def part_one(text: str) -> int:
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
    return total_middle_page_number

def part_two(text: str) -> int:
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
                changed = True
        if changed:
            while True:
                new_sorting = False
                for n in range(len(order_pages) - 1):
                    if before_element := rule_book.get(order_pages[n]):
                        for el in before_element:
                            for i in range(len(order_pages)):
                                if el == order_pages[i] and n < i:
                                    order_pages[n], order_pages[i] = order_pages[i], order_pages[n]
                                    new_sorting = True
                                    break
                if not new_sorting:
                    break

        if changed:
            total_middle_page_number += int(order_pages[int(len(order_pages) / 2)])
    return total_middle_page_number


if __name__ == "__main__":
    input = parse()
    print("part one: ", part_one(input))
    print("part two: ", part_two(input))
