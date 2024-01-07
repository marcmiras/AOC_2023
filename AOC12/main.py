def read_input(file_name="input.txt"):
    try:
        with open(file_name) as f:
            return f.read().splitlines()
    except FileNotFoundError:
        print("Error: File'", file_name, "' not found.")
        return None


def count_total_arrangements(lines):
    total_arrangements = 0

    for line in lines:
        record, groups = line.split(' ')

        group_sizes = []
        for size in groups.split(','):
            group_sizes.append(int(size))

        total_springs = sum(group_sizes)
        unassigned_springs = total_springs - record.count('#')

        unassigned_positions = []
        for i, char in enumerate(record):
            if char == '?':
                unassigned_positions.append(i)

        arrangements_count = count_arrangements(record, unassigned_positions, unassigned_springs, group_sizes)
        total_arrangements += arrangements_count

    return total_arrangements


def count_arrangements(record, unassigned_positions, unassigned_springs, group_sizes):
    arrangements_counter = 0

    stack = [(unassigned_positions, unassigned_springs, [])]

    while stack:
        positions, springs_left, current_assignment = stack.pop()

        if springs_left == 0:
            new_record = apply_assignment(record, current_assignment)
            if is_valid(new_record, group_sizes):
                arrangements_counter += 1
            continue

        if not positions:
            continue

        stack.append((positions[1:], springs_left, current_assignment))
        stack.append((positions[1:], springs_left - 1, current_assignment + [positions[0]]))

    return arrangements_counter


def apply_assignment(record, assignment):
    new_record = list(record)
    for position in assignment:
        new_record[position] = '#'
    return ''.join(new_record)


def is_valid(record, expected_group_sizes):
    actual_group_sizes, current_group_size = [], 0

    for char in record:
        if char == '#':
            current_group_size += 1
        elif current_group_size > 0:
            actual_group_sizes.append(current_group_size)
            current_group_size = 0

    if current_group_size > 0:
        actual_group_sizes.append(current_group_size)

    return actual_group_sizes == expected_group_sizes


# ONLY PART 1!
def main():
    lines = read_input()

    print("Part 1:", count_total_arrangements(lines))


if __name__ == "__main__":
    main()
