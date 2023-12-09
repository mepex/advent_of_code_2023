import re
import numpy

f = "input.txt"
times = []
distances = []


# give 5-char string, determine hand type:
# 5 of a kind: 7
# 4 of a kind: 6
# Full house: 5
# 3 of a kind: 4
# Two pair: 3
# One pair: 2
# High card: 1
def hand_type(str):
    cards = "AKQJT98765432"
    if all(c == str[0] for c in str):
        return 7
    nums = []
    # count the number of incidents of a specific card, store in array
    for c in cards:
        num = str.count(c)
        nums.append(str.count(c))
        if num == 4:
            return 6;
    # array now only has 3s and 2s at most
    if nums.count(3) == 1 and nums.count(2) == 1:
        return 5
    if nums.count(3) == 1:
        return 4
    if nums.count(2) == 2:
        return 3
    if nums.count(2) == 1:
        return 2
    else:
        return 1




# return 0 or 1, indicating which hand of the same type is higher
def tiebreak(s1, s2):
  pass


# bubble sort by 3rd element in tuple
def sort_tuple(tup):
    cards = "AKQJT98765432"
    # getting length of list of tuples
    lst = len(tup)
    for i in range(0, lst):
        for j in range(0, lst - i - 1):
            if (tup[j][2] > tup[j + 1][2]):
                temp = tup[j]
                tup[j] = tup[j + 1]
                tup[j + 1] = temp

    print(f"Before tiebreaks: {tup}")
    # do another round of sorting, iterating through the cards for tiebreaks
    for i in range(0, lst):
        for j in range(0, lst - i - 1):
            a = tup[j]
            b = tup[j+1]
            if a[2] == b[2]:
                for k in range(len(a[0])):
                    if cards.index(a[0][k]) < cards.index(b[0][k]):
                        # swap, because the lowest hands are first
                        temp = tup[j]
                        tup[j] = tup[j + 1]
                        tup[j + 1] = temp
                        break
                    elif cards.index(a[0][k]) > cards.index(b[0][k]):
                        # correct order
                        break
    return tup

hands = []
with open(f) as fp:
    for line in fp:
        result = re.match(r"([A-Z2-9]+) (\d+)", line.strip())
        # tuple is hand, bid, rank
        hands.append((result.group(1), int(result.group(2)), hand_type(result.group(1))))

# now sort the tuples based on rank
sort_tuple(hands)
print(hands)
total = 0
for i in range(len(hands)):
    m = i + 1
    total = total + (hands[i][1] * m)

print(f"Part 1 total: {total}")

# part 2 : Js are jokers
# give 5-char string, determine hand type:
# 5 of a kind: 7
# 4 of a kind: 6
# Full house: 5
# 3 of a kind: 4
# Two pair: 3
# One pair: 2
# High card: 1
def hand_type2(str):
    cards = "AKQT98765432"
    if all(c == str[0] for c in str):
        return 7
    jokers = str.count("J")
    nums = []
    # count the number of incidents of a specific card, store in array
    for c in cards:
        num = str.count(c)
        nums.append(str.count(c))
        if num == 4:
            return 6 if jokers == 0 else 7;
    # array now only has 3s and 2s at most
    if nums.count(3) == 1 and nums.count(2) == 1:
        return 5 if jokers == 0 else 6
    if nums.count(3) == 1:
        # either 3 of a kind, 4 of a kind, 5 of a kind depending on number of jokers
        r = [4, 6, 7]
        return r[jokers]
    if nums.count(2) == 2:
        # either two pair or full house
        r = [3, 5]
        return r[jokers]
    if nums.count(2) == 1:
        # either one pair, three of a kind, four of a kind, or five of a kind
        r = [2, 4, 6, 7]
        return r[jokers]
    else:
        # either high card, one pair, three of a kind, four of a kind, or five of a kind
        r = [1, 2, 4, 6, 7]
        return r[jokers]

# bubble sort by 3rd element in tuple
def sort_tuple2(tup):
    cards = "AKQT98765432J"
    # getting length of list of tuples
    lst = len(tup)
    for i in range(0, lst):
        for j in range(0, lst - i - 1):
            if (tup[j][2] > tup[j + 1][2]):
                temp = tup[j]
                tup[j] = tup[j + 1]
                tup[j + 1] = temp

    print(f"Before tiebreaks: {tup}")
    # do another round of sorting, iterating through the cards for tiebreaks
    for i in range(0, lst):
        for j in range(0, lst - i - 1):
            a = tup[j]
            b = tup[j+1]
            if a[2] == b[2]:
                for k in range(len(a[0])):
                    if cards.index(a[0][k]) < cards.index(b[0][k]):
                        # swap, because the lowest hands are first
                        temp = tup[j]
                        tup[j] = tup[j + 1]
                        tup[j + 1] = temp
                        break
                    elif cards.index(a[0][k]) > cards.index(b[0][k]):
                        # correct order
                        break
    return tup

hands = []
with open(f) as fp:
    for line in fp:
        result = re.match(r"([A-Z2-9]+) (\d+)", line.strip())
        # tuple is hand, bid, rank
        hands.append((result.group(1), int(result.group(2)), hand_type2(result.group(1))))

# now sort the tuples based on rank
sort_tuple2(hands)
print(hands)
total = 0
for i in range(len(hands)):
    m = i + 1
    total = total + (hands[i][1] * m)

print(f"Part 2 total: {total}")





