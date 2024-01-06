def read_input(file_name="input.txt"):
    try:
        with open(file_name, "r") as f:
            lines = f.readlines()
            num_list = []

            for line in lines:
                numbers = [int(number) for number in line.strip().split()]
                num_list.append(numbers)

            return num_list

    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        return None


def calc_partial_results(values):
    partial_result_1 = values[-1]
    partial_result_2 = values[0]

    for _ in range(len(values) - 1):
        differences = [values[i] - values[i - 1] for i in range(1, len(values))]
        values = differences

        partial_result_1 += values[-1]
        partial_result_2 = values[0] - partial_result_2

    return partial_result_1, partial_result_2


def calc_final_results(nums, part):
    total_part1, total_part2 = 0, 0

    for num in nums:
        part1, part2 = calc_partial_results(num)
        total_part1 += part1
        total_part2 += part2

    return total_part1 if part == 1 else total_part2


def part1(input_data):
    return calc_final_results(input_data, part=1)


def part2(input_data):
    return calc_final_results(input_data, part=2)


def main():
    input_data = read_input()

    print("Part 1:", part1(input_data))
    print("Part 2:", part2(input_data))

    return 0


if __name__ == "__main__":
    main()
