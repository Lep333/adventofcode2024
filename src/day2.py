import copy

def parse(input: str) -> list:
    input = input.split("\n")
    reports = []
    for line in input:
        reports.append([int(el) for el in line.split()])

    return reports

def part_one(reports: list[list[int]]) -> int:
    safe_report_sum = 0
    for report in reports:
        if report_is_safe(report):
            safe_report_sum += 1
    return safe_report_sum

def part_two(reports: list[list[int]]) -> int:
    safe_report_sum = 0
    safe_report_list = []
    for report in reports:
        if report_is_safe(report):
            safe_report_sum += 1
            safe_report_list.append(report)
        else:
            for i in range(len(report)):
                dampener_used = copy.copy(report)
                dampener_used.pop(i)
                if report_is_safe(dampener_used):
                    # print(report, dampener_used)
                    safe_report_list.append(report)
                    safe_report_sum += 1
                    break
    return safe_report_sum

def report_is_safe(report: list[int]) -> bool:
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
    return safe_report

if __name__ == "__main__":
    input_file_path = "input/day2input.txt"
    text = ""
    with open(input_file_path, "r") as f:
        text = f.read()
    input = parse(text)
    print("safe reports part one: ", part_one(input))
    print("safe reports part two: ", part_two(input))