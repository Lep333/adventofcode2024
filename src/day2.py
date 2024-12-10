input_file_path = "input/day2input.txt"

def parse() -> list:
    reports = []
    with open(input_file_path, "r") as f:
        for line in f:
            reports.append([int(el) for el in line.split()])

    return reports

def main():
    part_one()
    part_two()

def part_one():
    reports = parse()

    safe_report_sum = 0
    for report in reports:
        inc = False
        dec = False
        safe_report = True
        for i in range(len(report) - 1):
            curr_element = report[i]
            next_element = report[i + 1]

            if curr_element < next_element:
                inc = True
            if curr_element > next_element:
                dec = True
            diff = abs(curr_element - next_element)
            if diff > 3 or diff == 0:
                safe_report = False
        if inc and dec:
            safe_report = False
        if safe_report:
            safe_report_sum += 1
    print("safe reports: ", safe_report_sum)

def part_two():
    reports = parse()

    safe_report_sum = 0
    for report in reports:
        inc = False
        dec = False
        problem_dampener_avail = True
        safe_report = True
        for i in range(len(report) - 1):
            curr_element = report[i]
            next_element = report[i + 1]

            if curr_element < next_element:
                if dec and problem_dampener_avail:
                    problem_dampener_avail = False
                    continue
                inc = True
            if curr_element > next_element:
                if inc and problem_dampener_avail:
                    problem_dampener_avail = False
                    continue
                else:
                    dec = True
            diff = abs(curr_element - next_element)
            if diff > 3 or diff == 0:
                if problem_dampener_avail:
                    problem_dampener_avail = False
                else:
                    safe_report = False
        if inc and dec:
            safe_report = False
        if safe_report:
            safe_report_sum += 1
    print("safe reports: ", safe_report_sum)


if __name__ == "__main__":
    main()