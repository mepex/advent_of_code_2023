import re



idx = 0
part_nums = []
symbols = []
total_points = 0
idx = 0


seeds = []
seed2soil = False
soil2fert = False
fert2water = False
water2light = False
light2temp = False
temp2humid = False
humid2loc = False

s2s = []
s2f = []
f2w = []
w2l = []
l2t = []
t2h = []
h2l = []

def processLine(l):
    result = re.match(r"(\d+) (\d+) (\d+)", l)
    if result:
        return True, int(result.group(1)), int(result.group(2)), int(result.group(3))
    else:
        return False, None, None, None

f = "input.txt"

with open(f) as fp:
    for line in fp:
        result = re.match(r"seeds: (.*)", line.strip())
        if result:
            seeds = result.group(1).split()
            for i in range(len(seeds)):
                seeds[i] = int(seeds[i])

        if re.match(r"seed-to-soil map:", line.strip()):
            seed2soil = True
        if re.match(r"soil-to-fertilizer map:", line.strip()):
            soil2fert = True
        if re.match(r"fertilizer-to-water map:", line.strip()):
            fert2water = True
        if re.match(r"water-to-light map:", line.strip()):
            water2light = True
        if re.match(r"light-to-temperature map:", line.strip()):
            light2temp = True
        if re.match(r"temperature-to-humidity map:", line.strip()):
            temp2humid = True
        if re.match(r"humidity-to-location map:", line.strip()):
            humid2loc = True

        (valid, dest, source, length) = processLine(line.strip())

        if valid:
            if humid2loc:
                h2l.append((dest, source, length))
            elif temp2humid:
                t2h.append((dest, source, length))
            elif light2temp:
                l2t.append((dest, source, length))
            elif water2light:
                w2l.append((dest, source, length))
            elif fert2water:
                f2w.append((dest, source, length))
            elif soil2fert:
                s2f.append((dest, source, length))
            elif seed2soil:
                s2s.append((dest, source, length))

print(f"seeds: {seeds}")
print(f"s2s : {s2s}")
print(f"s2f : {s2f}")
print(f"f2w : {f2w}")
print(f"w2l : {w2l}")
print(f"l2t : {l2t}")
print(f"t2h : {t2h}")
print(f"h2l : {h2l}")


def findLocation(n):
    global s2s, s2f, f2w, w2l, l2t, t2h, h2l
    names = ["soil", "fertilizer", "water", "light", "temp", "humidity", "location"]
    i = 0
    exit = n
    print(f"seed {s} :", end = "")
    for a in (s2s, s2f, f2w, w2l, l2t, t2h, h2l):
        entry = exit
        for dest, source, length in a:
            if entry >= source and entry < source + length:
                exit = dest + (entry - source)
        print(f" {names[i]} is {exit},", end = "")
        i = i + 1

    print("")
    return exit

locs = []
for s in seeds:
    locs.append(findLocation(s))

print(f"part 1 nearest location is {min(locs)}")

seeds = []
with open(f) as fp:
    for line in fp:
        result = re.match(r"seeds: (.*)", line.strip())
        if result:
            s = result.group(1).split()
            for i in range(int(len(s)/2)):
                start = int(s[2*i])
                end = start + int(s[2*i+1])
                seeds.append((start, end))

print(f"part 2 seeds: {seeds}")

# have to start a location 1 and work backwards to seed, then see if seed is in list

def findSeed(n):
    global s2s, s2f, f2w, w2l, l2t, t2h, h2l
    names = ["location", "humidity", "temp", "light", "water", "fertilizer", "soil", "seed"]
    i = 0
    exit = n
    #print(f"location {n}: ", end="")
    for a in (h2l, t2h, l2t, w2l, f2w, s2f, s2s):
        entry = exit
        for dest, source, length in a:
            if entry >= dest and entry < dest + length:
                exit = source + (entry - dest)
        #print(f" {names[i]}:{exit}, ", end="")
        i = i + 1
    #print("")

    return exit

for loc in range(100000000):
    s = findSeed(loc)
    for start, end in seeds:
        if s >= start and s < end:
            print(f"Found lowest location: {loc} for seed {s}")
            exit()
    if loc % 1000000 == 0:
        print(f"searched {loc} locations...")








