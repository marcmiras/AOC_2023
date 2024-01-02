with open("games.txt", "r", encoding="utf-8") as file:
    games = [line.strip().split(':')[1] for line in file.readlines()]

max_numbers = {"red": 12, "green": 13, "blue": 14}


def get_min_numbers(line):
    draws = line.split(';')
    max_red = max_green = max_blue = 0

    for draw in draws:
        for cube in draw.split(','):
            number, color = cube.split()
            number = int(number)

            if color == "red":
                max_red = max(max_red, number)
            elif color == "green":
                max_green = max(max_green, number)
            elif color == "blue":
                max_blue = max(max_blue, number)

    return max_red, max_green, max_blue


def count_valid_numbers(line, ids):
    draws = line.split(';')

    for draw in draws:
        for cube in draw.split(','):
            number, color = cube.split()
            if max_numbers[color] < int(number):
                return 0
    return ids


count = 0
mult_sum = 0

for i, game in enumerate(games, start=1):
    count += count_valid_numbers(game, i)
    min_numbers = get_min_numbers(game)
    mult_sum += min_numbers[0] * min_numbers[1] * min_numbers[2]

print("Part 1:", count)
print("Part 2:", mult_sum)