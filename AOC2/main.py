with open("games.txt", "r", encoding="utf-8") as filePath:
    games = [line.strip().split(':')[1] for line in filePath.readlines()]

maxNum = {"red": 12, "green": 13, "blue": 14}


def count_nums(game, ids):
    draws = game.split(';')
    for draw in draws:
        for cube in draw.split(','):
            n, color = cube.split()
            if maxNum[color] < int(n):
                return 0
    return ids


count = 0
for i, game in enumerate(games):
    count += count_nums(game, i + 1)
print("Part 1:", count)
