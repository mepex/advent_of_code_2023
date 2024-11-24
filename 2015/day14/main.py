import re

f = "input.txt"
deer = []
speeds = []
works = []
rests = []
count = 0
with open(f) as fp:
    for line in fp:
        line = line.strip()
        m = re.search(r'(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds', line)
        if m:
            deer.append(m.group(1))
            speeds.append(int(m.group(2)))
            works.append(int(m.group(3)))
            rests.append(int(m.group(4)))

distances = []
time = 2503
totals = []
for i in range(len(deer)):
    period = works[i] + rests[i]
    distance_per_period = speeds[i] * works[i]
    periods = time // period
    partial = speeds[i] * works[i] if (time % period) > works[i] else (time % period) * speeds[i]
    totals.append(partial + (distance_per_period * periods))

print(totals)
print(max(totals))

points = [0] * len(deer)
for t in range(1, time):
    distances = []
    for i in range(len(deer)):
        period = works[i] + rests[i]
        distance_per_period = speeds[i] * works[i]
        periods = t // period
        partial = speeds[i] * works[i] if (t % period) > works[i] else (t % period) * speeds[i]
        distances.append(partial + (distance_per_period * periods))
    furthest = max(distances)
    # find all indices in array that have value furthest, there can be a tie, and both get points
    indices = [i for i, x in enumerate(distances) if x == furthest]
    for index in indices:
        points[index] += 1

print(max(points))


