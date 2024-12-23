import math

def part_one(secrets: list[int], n_new_secrets: int) -> int:
    total = 0
    for secret in secrets:
        sec = secret
        for _ in range(n_new_secrets):
            sec = new_secret(sec)
        total += sec
    return total

def part_two(secrets: list[int], n_new_secrets: int) -> int:
    mem = dict()
    for secret in secrets:
        sec = secret
        first_seq = []
        cons_changes = []
        prize = sec % 10
        old_prize = None
        for _ in range(n_new_secrets):
            sec = new_secret(sec)
            old_prize = prize
            prize = sec % 10
            cons_changes.append(prize - old_prize)
            if len(cons_changes) > 4:
                cons_changes.pop(0)
            if len(cons_changes) == 4:
                cons_changes_str = str(cons_changes)
                if not cons_changes_str in first_seq:
                    first_seq.append(cons_changes_str)
                    if mem.get(cons_changes_str):
                        mem[cons_changes_str] += prize
                    else:
                        mem[cons_changes_str] = prize

    test = list(mem.values())
    test.sort(reverse=True)
    return test[0]

def new_secret(secret: int) -> int:
    prune_const = 16777216
    result = secret * 64
    new_secret = result ^ secret
    new_secret = new_secret % prune_const
    result = math.floor(new_secret / 32)
    new_secret = result ^ new_secret
    new_secret = new_secret % prune_const
    result = new_secret * 2048
    new_secret = result ^ new_secret
    new_secret = new_secret % prune_const
    return new_secret

if __name__ == "__main__":
    input_file_path = "input/day22input.txt"
    n_new_secrets = 2000
    input = []
    with open(input_file_path, "r") as f:
        input = f.readlines()
    input = [int(el) for el in input]
    print("part one: ", part_one(input, n_new_secrets))
    print("part two: ", part_two(input, n_new_secrets))
