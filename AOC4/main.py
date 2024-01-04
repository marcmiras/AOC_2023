def part1(lines):
    points = 0

    for line in lines:
        value = 0

        winning_nums, card_nums = line.split(":")[1].split("|")

        winning_nums = [int(num) for num in winning_nums.split()]
        card_nums = [int(num) for num in card_nums.split()]

        matches = 0

        for win_num in winning_nums:
            if win_num in card_nums:
                if matches != 0:
                    value *= 2
                else:
                    value = 1
                matches += 1
        points += value

    return points


def part2(lines):
    points = 0
    num_cards = [1] * len(lines)

    for i in range(len(lines)):
        num_cards[i] = 1

    for i, line in enumerate(lines):
        value = 0

        winning_nums, card_nums = line.split(":")[1].split("|")

        winning_nums = [int(num) for num in winning_nums.split()]
        card_nums = [int(num) for num in card_nums.split()]

        matches = 0

        for win_num in winning_nums:
            if win_num in card_nums:
                if matches != 0:
                    value *= 2
                else:
                    value = 1
                matches += 1
                num_cards[i + matches] += 1 * num_cards[i]

        points += value

    return sum(num_cards)


def main():
    with open("input.txt", "r") as f:
        cards = f.readlines()

    print("Part 1:", part1(cards))
    print("Part 2:", part2(cards))


if __name__ == "__main__":
    main()
