import re

maxes = {
    "red" : 12,
    "green" : 13,
    "blue" : 14
}
sum = 0
with open("input.txt") as fp:
    for line in fp:
        result = re.search(r"Game (\d+): (.*)", line.strip())
        game_id = int(result.group(1))
        sets = result.group(2).split(';')
        possible = True
        for s in sets:
            colors = re.findall("((\d+) (green|red|blue))", s.strip())
            for c in colors:
                if int(c[1]) > maxes[c[2]]:
                    possible = False
        if possible:
            sum = sum + game_id

print(f"part 1 sum is {sum}")

sum = 0
with open("input.txt") as fp:
    for line in fp:
        result = re.search(r"Game (\d+): (.*)", line.strip())
        game_id = int(result.group(1))
        sets = result.group(2).split(';')
        possible = True
        game = {
            "blue" : 0,
            "red" : 0,
            "green" : 0
        }
        for s in sets:
            colors = re.findall("((\d+) (green|red|blue))", s.strip())
            for c in colors:
                if int(c[1]) > game[c[2]]:
                    game[c[2]] = int(c[1])
        sum = sum + (game["blue"] * game["red"] * game["green"])

print(f"part 1 sum is {sum}")





