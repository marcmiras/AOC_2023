def read_input_file(input_filename="input.txt"):
    input_lines = []
    try:
        with open(input_filename, "r") as input_file:
            for line in input_file:
                input_lines.append(line.strip("\n"))
    except FileNotFoundError:
        print(f"Error: File '{input_filename}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return input_lines


def extract_numbers(lines):
    numbers = []
    num_lines, line_length = len(lines), len(lines[0])

    for i in range(num_lines):
        j = 0
        while j < line_length:
            if lines[i][j].isdigit():
                start_index = j
                while j < line_length and lines[i][j].isdigit():
                    j += 1
                j -= 1
                numbers.append((int(lines[i][start_index:j + 1]), (i, start_index, j)))
            j += 1

    return numbers


def calc_adjacent_numbers(numbers, lines):
    total_sum = 0
    num_lines, line_length = len(lines), len(lines[0])

    for num in numbers:
        part_number = any(
            not (lines[i][j].isdigit() or lines[i][j] == ".")
            for i in range(num[1][0] - 1, min(num[1][0] + 2, num_lines))
            for j in range(num[1][1] - 1, min(num[1][2] + 2, line_length))
        )

        if part_number:
            total_sum += num[0]

    return total_sum


def calc_gear_ratio(lines):
    num_lines = len(lines)
    line_len = len(lines[0])

    numbers = []
    for i in range(len(lines)):
        j = 0
        while j < line_len:
            if lines[i][j].isdecimal():
                start_index = j
                current_number = ""
                while j < line_len and lines[i][j].isdecimal():
                    current_number += lines[i][j]
                    j += 1
                j -= 1
                numbers.append((int(current_number), (i, start_index, j)))

            j += 1

    gears = {}
    for num in numbers:
        for i in range(num[1][0] - 1, num[1][0] + 2):
            if 0 <= i < num_lines:
                for j in range(num[1][1] - 1, num[1][2] + 2):
                    if 0 <= j < line_len:
                        if lines[i][j] == "*":
                            if (i, j) not in gears:
                                gears[(i, j)] = []
                            gears[(i, j)].append(num[0])

    gear_ratio_sum = 0
    for gear in gears:
        if len(gears[gear]) == 2:
            product = 1
            for value in gears[gear]:
                product *= value
            gear_ratio_sum += product

    return gear_ratio_sum


def main():
    input_lines = read_input_file()

    numbers_part1 = extract_numbers(input_lines)
    total_sum_part1 = calc_adjacent_numbers(numbers_part1, input_lines)
    print("Part 1:", total_sum_part1)

    gear_ratio_sum = calc_gear_ratio(input_lines)
    print("Part 2:", gear_ratio_sum)


if __name__ == "__main__":
    main()
