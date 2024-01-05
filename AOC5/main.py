def read_input():
    try:
        with open("input.txt", "r") as f:
            return f.read().splitlines()
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"Error: An unexpected error occurred - {e}")


def extract_ints(line):
    result = []
    current_number = ""

    for char in line:
        if char.isdigit():
            current_number += char
        elif current_number:
            result.append(int(current_number))
            current_number = ""

    if current_number:
        result.append(int(current_number))

    return result


def find_loc(maps, input_value):
    value = input_value

    for source_map in maps:
        for source_range, dest_range in source_map.items():
            if value in source_range:
                value = dest_range.start + (value - source_range.start)
                break

    return value


def reverse_find_loc(value, maps):
    for source_map in reversed(maps):
        for source_range, dest_range in source_map.items():
            if value in dest_range:
                value = source_range.start + (value - dest_range.start)
                break
    return value


def init_maps(seed_input):
    maps = []

    iter_lines = iter(seed_input)
    next(iter_lines)
    next(iter_lines)

    for line in iter_lines:
        if 'map' in line:
            maps.append(dict())
        elif line != '':
            dest, source, length = [int(value) for value in line.split()]
            source_range = range(source, source + length)
            dest_range = range(dest, dest + length)
            maps[-1][source_range] = dest_range

    return maps


def part1(seed_input):
    maps = init_maps(seed_input)
    seeds = extract_ints(seed_input[0])
    locations = []

    for seed in seeds:
        locations.append(find_loc(maps, seed))

    return min(locations)


def part2(seed_input):
    location = 0
    maps = init_maps(seed_input)
    seeds = extract_ints(seed_input[0])
    seed_ranges = []

    for i in range(0, len(seeds) - 1, 2):
        start = seeds[i]
        length = seeds[i + 1]
        seed_range = range(start, start + length)
        seed_ranges.append(seed_range)

    while True:
        potential_seed = reverse_find_loc(location, maps)

        if any(potential_seed in seed_range for seed_range in seed_ranges):
            break

        location += 1

    return location


def main():
    seed_input = read_input()

    print("Part 1:", part1(seed_input))
    print("Part 2:", part2(seed_input))

    return 0


if __name__ == "__main__":
    main()
