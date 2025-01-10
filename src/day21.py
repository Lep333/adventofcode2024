def part_one(input: list[str]) -> int:
    numeric_keypad = {}
    numeric_keypad["0"] = (1, 0)
    numeric_keypad["A"] = (2, 0)
    numeric_keypad["1"] = (0, 1)
    numeric_keypad["2"] = (1, 1)
    numeric_keypad["3"] = (2, 1)
    numeric_keypad["4"] = (0, 2)
    numeric_keypad["5"] = (1, 2)
    numeric_keypad["6"] = (2, 2)
    numeric_keypad["7"] = (0, 3)
    numeric_keypad["8"] = (1, 3)
    numeric_keypad["9"] = (2, 3)

    
