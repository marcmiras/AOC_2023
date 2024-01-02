import math


def compute_interval(time, distance):
    result = time ** 2 - 4 * distance

    if result < 0:
        return 0

    root1 = (-time - math.sqrt(result)) / 2
    root2 = (-time + math.sqrt(result)) / 2

    interval = round(root2 - root1)

    if root2 == root1:
        interval -= 1

    return max(interval, 0)


def read_input_file(file_path):
    with open(file_path, "r") as file_data:
        return [line.strip() for line in file_data]


def parse_input_line(line):
    return [int(value) for value in line[10:].split()]


def main():
    input_file_path = "input.txt"
    input_lines = read_input_file(input_file_path)

    time_list = parse_input_line(input_lines[0])
    distance_list = parse_input_line(input_lines[1])

    part1_result = 1
    for i in range(len(time_list)):
        part1_result *= compute_interval(time_list[i], distance_list[i])

    time = int("".join(input_lines[0][10:].split()))
    distance = int("".join(input_lines[1][10:].split()))
    part2_result = compute_interval(time, distance)

    print(f"Part 1 Result: {part1_result}")
    print(f"Part 2 Result: {part2_result}")


if __name__ == "__main__":
    main()
