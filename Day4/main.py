import re



idx = 0
part_nums = []
symbols = []
total_points = 0
idx = 0

f = "input.txt"

with open(f) as fp:
    for line in fp:
        result = re.search(r": (.*) \| (.*)", line.strip())
        winners = result.group(1).split()
        my_nums = result.group(2).split()
        num_winners = 0
        for w in winners:
            if w in my_nums:
                num_winners = num_winners + 1
        points = pow(2, num_winners-1) if num_winners > 0 else 0
        total_points = total_points + points
        idx = idx + 1

print(f"Part 1 total points: {total_points}")

cards = [1] * (idx + 1)
cards[0] = 0

with open(f) as fp:
    for line in fp:
        result = re.search(r"Card\s+(\d+): (.*) \| (.*)", line.strip())
        card_num = int(result.group(1))
        winners = result.group(2).split()
        my_nums = result.group(3).split()
        num_winners = 0
        for w in winners:
            if w in my_nums:
                num_winners = num_winners + 1
        for i in range(num_winners):
            cards[card_num + 1 + i] = cards[card_num + 1 + i] + cards[card_num]

print(f"Part 2 total cards: {sum(cards)}")