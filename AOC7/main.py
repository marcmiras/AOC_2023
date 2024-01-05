
def read_input():
    try:
        with open("input.txt", "r") as file:
            content = file.read().strip()
        return content
    except FileNotFoundError:
        print("Error: File 'input.txt' not found.")
    except Exception as e:
        print(f"Error: An unexpected error occurred - {e}")


def parse_hands(hands_input):
    hands = []
    for line in hands_input.split("\n"):
        card, bid = line.split(" ")
        hands.append((card, int(bid)))
    return hands


def calc_order(part_two):
    card_values = "J23456789TQKA" if part_two else "23456789TJQKA"
    return {value: i for i, value in enumerate(card_values)}


def is_single(card_counts, jokers):
    return len(card_counts) < 2


def is_four_of_a_kind(card_counts, jokers):
    return max(card_counts.values()) + jokers == 4


def is_full_house(card_counts, jokers):
    values = list(card_counts.values())

    if len(values) == 2:
        count_2 = 0
        count_3 = 0

        for value in values:
            if value == 2:
                count_2 += 1
            elif value == 3:
                count_3 += 1

        if (count_2 == 1 and count_3 == 1) or (count_2 == 2 and jokers == 1):
            return True

    return False


def is_three_of_a_kind(card_counts, jokers):
    for value in card_counts.values():
        if value == (3 - jokers):
            return True
    return False


def is_two_pair(card_counts, jokers):
    values = list(card_counts.values())

    if 2 in values and values.count(2) == 2:
        return True
    elif jokers > 0 and 2 in values:
        return True

    return False


def is_one_pair(card_counts, jokers):
    for value in card_counts.values():
        if value == (2 - jokers):
            return True
    return False


def categorize_hands(hands_data, is_part_two):
    sorted_hands = []
    for _ in range(7):
        sorted_hands.append([])

    for card, bid in hands_data:
        card_counts = {}
        for c in card:
            if c in card_counts:
                card_counts[c] += 1
            else:
                card_counts[c] = 1

        if is_part_two:
            jokers = card_counts.get("J", 0)
            if "J" in card_counts:
                del card_counts["J"]
        else:
            jokers = 0

        hand_type_index = 6
        for i in range(6):
            if i == 0 and is_single(card_counts, jokers):
                hand_type_index = i
                break
            elif i == 1 and is_four_of_a_kind(card_counts, jokers):
                hand_type_index = i
                break
            elif i == 2 and is_full_house(card_counts, jokers):
                hand_type_index = i
                break
            elif i == 3 and is_three_of_a_kind(card_counts, jokers):
                hand_type_index = i
                break
            elif i == 4 and is_two_pair(card_counts, jokers):
                hand_type_index = i
                break
            elif i == 5 and is_one_pair(card_counts, jokers):
                hand_type_index = i
                break

        sorted_hands[hand_type_index].append((card, bid))

    return sorted_hands


def sort_hands_by_order(sorted_hands, order):
    for i in range(len(sorted_hands)):
        hands_list = sorted_hands[i]
        hands_list.sort(key=lambda x: [order[c] for c in x[0]])


def calculate_final_score(sorted_hands):
    total_score = 0
    index = 1

    for hands_list in reversed(sorted_hands):
        for card, bid in hands_list:
            total_score += index * bid
            index += 1

    return total_score


def solve(is_part_two):
    hands_data = parse_hands(read_input())
    sorted_hands = categorize_hands(hands_data, is_part_two)
    order = calc_order(is_part_two)
    sort_hands_by_order(sorted_hands, order)
    return calculate_final_score(sorted_hands)


def part1():
    return solve(False)


def part2():
    return solve(True)


def main():
    print("Part 1:", part1())
    print("Part 2:", part2())
    return 0


if __name__ == "__main__":
    main()
