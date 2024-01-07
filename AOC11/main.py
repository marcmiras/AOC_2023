def parse_input(file_name="input.txt"):
    try:
        with open(file_name) as f:
            lines = f.read().splitlines()
        return lines
    except FileNotFoundError:
        print("Error: File", file_name, "' not found.")
        return None


def set_galaxies(grid):
    full = set()
    x_axis = set(range(len(grid[0])))
    y_axis = set(range(len(grid)))

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "#":
                full.add((x, y))
                if x in x_axis:
                    x_axis.remove(x)
                if y in y_axis:
                    y_axis.remove(y)

    return full, x_axis, y_axis


def solve_dist(full, x_axis, y_axis, is_part2):
    part1, part2 = 0, 0

    for galaxy in full.copy():
        full.remove(galaxy)

        for other_galaxy in full:
            left_h, right_h = sorted([galaxy[0], other_galaxy[0]])
            left_v, right_v = sorted([galaxy[1], other_galaxy[1]])
            sum_dist = right_h - left_h + right_v - left_v

            extra_h = sum(1 for x in x_axis if left_h < x < right_h)
            extra_v = sum(1 for y in y_axis if left_v < y < right_v)

            part1 += sum_dist + (sum_extra := extra_h + extra_v)
            part2 += sum_dist + sum_extra * 999999

    if not is_part2:
        return part1
    else:
        return part2


def part1(lines):
    positions = set_galaxies(lines)
    return solve_dist(positions[0], positions[1], positions[2], False)


def part2(lines):
    positions = set_galaxies(lines)
    return solve_dist(positions[0], positions[1], positions[2], True)


def main():
    lines = parse_input()

    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
    return 0


if __name__ == '__main__':
    main()
