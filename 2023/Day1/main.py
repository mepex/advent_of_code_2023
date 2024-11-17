import re

sum = 0
with open("input.txt") as fp:
    for line in fp:
        matches = re.findall("\d", line.strip())
        if len(matches) == 1:
            sum = sum + (int(matches[0]) * 10) + int(matches[0])
        else:
            sum = sum + (int(matches[0]) * 10) + int(matches[len(matches) - 1])

print(f"part 1 sum is {sum}")

num_dict = {
    "1" : 1,
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9,
    "one" : 1,
    "two" : 2,
    "three" : 3,
    "four" : 4,
    "five" : 5,
    "six" : 6,
    "seven" : 7,
    "eight" : 8,
    "nine" : 9
}

sum = 0
with open("input.txt") as fp:
    for line in fp:
        matches = re.findall("(?=(\d|one|two|three|four|five|six|seven|eight|nine))", line.strip())
        if len(matches) == 1:
            num = (num_dict[matches[0]] * 10) + num_dict[matches[0]]
        else:
            num = (num_dict[matches[0]] * 10) + num_dict[matches[len(matches) - 1]]
        sum = sum + num

print(f"part 2 sum is {sum}")



