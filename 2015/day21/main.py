from itertools import combinations
from math import ceil


# tuple is damage, armor, cost
weapons = [(4, 0, 8), (5, 0, 10), (6, 0, 25), (7, 0, 40), (8, 0, 74)]
armor = [(0, 0, 0), (0, 1, 13), (0, 2, 31), (0, 3, 53), (0, 4, 75), (0, 5, 102)]
rings = [(0, 0, 0), (0, 0, 0), (1, 0, 25), (2, 0, 50), (3, 0, 100), (0, 1, 20), (0, 2, 40), (0, 3, 80)]


def is_win(damage, armor):
    opp_damage = 8
    opp_armor = 2
    opp_hitpoints = 100
    my_hitpoints = 100
    damage_per_turn = 1 if opp_armor >= damage else damage - opp_armor
    turns_to_kill = ceil(opp_hitpoints / damage_per_turn)
    injury_per_turn = 1 if armor >= opp_damage else opp_damage - armor
    turns_to_die = ceil(my_hitpoints / injury_per_turn)
    if turns_to_kill <= turns_to_die:
        return True
    return False

min_gold = 1e6

for w in weapons:
    for a in armor:
        for r in combinations(rings, 2):
            dam = w[0] + r[0][0] + r[1][0]
            arm = a[1] + r[0][1] + r[1][1]
            gold = w[2] + a[2] + r[0][2] + r[1][2]
            if is_win(dam, arm):
                if gold < min_gold:
                    min_gold = gold
                    print(f"found answer ${gold}: {w} {a} {r}")

print(f"part 1: {min_gold}")

max_gold = 0
for w in weapons:
    for a in armor:
        for r in combinations(rings, 2):
            dam = w[0] + r[0][0] + r[1][0]
            arm = a[1] + r[0][1] + r[1][1]
            gold = w[2] + a[2] + r[0][2] + r[1][2]
            if not is_win(dam, arm):
                if gold > max_gold:
                    max_gold = gold
                    print(f"found answer ${gold}: {w} {a} {r}")

print(f"part 2: {max_gold}")
