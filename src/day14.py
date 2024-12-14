import time
input_file_path = "input/day14input.txt"
no_of_cols = 101
no_of_rows = 103

def parse() -> list[tuple]:
    text = []
    roboters = []
    with open(input_file_path, "r") as f:
        text = f.read()
    text = text.replace("p=", "")
    text = text.replace("v=", "")
    text = text.replace(",", " ")
    text = text.split("\n")
    for roboter in text:
        pos_x, pos_y, vel_x, vel_y = roboter.split()
        roboters.append((int(pos_x), int(pos_y), int(vel_x), int(vel_y)))
    return roboters

def part_one(roboters: list[tuple]) -> int:
    # simulate 100 seconds
    no_of_seconds = 100

    for i in range(no_of_seconds):
        next_tick_roboters = []
        for roboter in roboters:
            new_pos_x = (roboter[0] + roboter[2]) % no_of_cols
            new_pos_y = (roboter[1] + roboter[3]) % no_of_rows
            robot_new_position = (new_pos_x, new_pos_y, roboter[2], roboter[3])
            next_tick_roboters.append(robot_new_position)
        roboters = next_tick_roboters

    # sum up result
    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0
    for roboter in roboters:
        if roboter[0] == int(no_of_cols / 2) or roboter[1] == int(no_of_rows / 2):
            continue
        if roboter[0] < no_of_cols / 2:
            if roboter[1] < no_of_rows / 2:
                q1 += 1
            else:
                q2 += 1
        else:
            if roboter[1] < no_of_rows / 2:
                q3 += 1
            else:
                q4 += 1

    return q1 * q2 * q3 * q4

def part_two(roboters: list[tuple]):
    # simulate 100 seconds
    no_of_seconds = 10000

    print_map(-1, roboters)
    for i in range(no_of_seconds):
        next_tick_roboters = []
        for roboter in roboters:
            new_pos_x = (roboter[0] + roboter[2]) % no_of_cols
            new_pos_y = (roboter[1] + roboter[3]) % no_of_rows
            robot_new_position = (new_pos_x, new_pos_y, roboter[2], roboter[3])
            next_tick_roboters.append(robot_new_position)
        roboters = next_tick_roboters
        print_map(i, roboters)

def print_map(second: int, roboters: list[tuple]):
    roboter_pos = {}

    overlap = False
    for robot in roboters:
        if roboter_pos.get(robot[0]):
            if roboter_pos[robot[0]].get(robot[1]):
                roboter_pos[robot[0]][robot[1]] += 1
                overlap = True
            else:
                roboter_pos[robot[0]][robot[1]] = 1
        else:
            roboter_pos[robot[0]] = {}
            roboter_pos[robot[0]][robot[1]] = 1

    if not overlap:
        frame = f"Elapsed time: {second + 1} \n"
        for y in range(no_of_rows):
            for x in range(no_of_cols):
                if num := roboter_pos.get(x):
                    if robos := num.get(y):
                        frame += "X"
                    else:
                        frame += "."
                else:
                    frame += "."
            frame += "\n"
        frame += "\n"
        print(frame)


if __name__ == "__main__":
    input = parse()
    print("safety factor: ", part_one(input))
    input = parse()
    part_two(input)