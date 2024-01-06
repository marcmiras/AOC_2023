import math


def read_input(file_path="input.txt"):
    try:
        with open(file_path) as f:
            lines = []
            for line in f.readlines():
                lines.append(line.strip("\r\n"))
        return lines
    except FileNotFoundError:
        print("Error: File '", file_path, "' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def build_mapping(values):
    result_map = {}
    start_i = 2
    for row in values[start_i:]:
        parts = row.split(" = ")
        if len(parts) == 2:
            key, values_part = parts[0].strip(), parts[1].strip("()")
            values_list = values_part.split(", ")
            if len(values_list) == 2:
                result_map[key] = (values_list[0], values_list[1])

    return result_map


def calculate_travel_steps(locs, dirs, mode):
    if mode == 1:
        start_positions = ["AAA"]
    else:
        start_positions = [x for x in locs if x.endswith("A")]

    result = []

    for start_pos in start_positions:
        steps = 0
        while True:
            if dirs[steps % len(dirs)] == "L":
                pos = locs[start_pos][0]
            else:
                pos = locs[start_pos][1]

            if mode == 1 and pos == "ZZZ":
                break
            elif mode == 2 and pos.endswith("Z"):
                break

            start_pos = pos
            steps += 1

        result.append(steps + 1)

    if mode == 1:
        return result[0]
    else:
        return math.lcm(*result)


def part1():
    return 0


def part2():
    return 0


def main():
    lines = read_input()

    locations = build_mapping(lines)
    directions = lines[0]

    answer_part1 = calculate_travel_steps(locations, directions, 1)
    answer_part2 = calculate_travel_steps(locations, directions, 2)

    print("Part 1:", answer_part1)
    print("Part 2:", answer_part2)

    return 0


if __name__ == "__main__":
    main()
