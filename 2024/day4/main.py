f = ("input.txt")
total = 0
grid = []
with open(f) as fp:
    for line in fp:
        line = line.strip()
        grid.append(line)

h = len(grid)
w = len(grid[0])

def look(grid, i, j):
    global lookfor
    s = len(lookfor)
    found = 0
    # east
    try:
        l = grid[i][j:j+s]
        found += 1 if l == lookfor else 0
    except IndexError:
        pass
    # west
    try:
        if j >= s-1:
            l = grid[i][j::-1][:4]
            found += 1 if l == lookfor else 0
    except IndexError:
        pass
    # north
    try:
        if i >= s - 1:
            l = grid[i][j] + grid[i-1][j] + grid[i-2][j] + grid[i-3][j]
            found += 1 if l == lookfor else 0
    except IndexError:
        pass
    # south
    try:
        l = grid[i][j] + grid[i+1][j] + grid[i+2][j] + grid[i+3][j]
        found += 1 if l == lookfor else 0
    except IndexError:
        pass
    # southeast
    try:
        l = grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2] + grid[i+3][j+3]
        found += 1 if l == lookfor else 0
    except IndexError:
        pass
    # southwest
    try:
        if j >= s-1:
            l = grid[i][j] + grid[i + 1][j - 1] + grid[i + 2][j - 2] + grid[i + 3][j - 3]
            found += 1 if l == lookfor else 0
    except IndexError:
        pass
    # northeast
    try:
        if i >= s-1:
            l = grid[i][j] + grid[i - 1][j + 1] + grid[i - 2][j + 2] + grid[i - 3][j + 3]
            found += 1 if l == lookfor else 0
    except IndexError:
        pass
    # northwest
    try:
        if i >= s-1 and j >= s-1:
            l = grid[i][j] + grid[i - 1][j - 1] + grid[i - 2][j - 2] + grid[i - 3][j - 3]
            found += 1 if l == lookfor else 0
    except IndexError:
        pass
    return found

lookfor = "XMAS"

found = 0
for i in range(h):
    for j in range(w):
        found += look(grid, i, j)

print(f"part 1 found : {found}")

def look2(grid, i, j):
    found = 0
    h = len(grid)
    w = len(grid[0])
    if i <= h - 3 and j <= w - 3:
        se = grid[i][j] + grid[i + 1][j + 1] + grid[i + 2][j + 2]
        sw = grid[i][j + 2] + grid[i + 1][j + 1] + grid[i + 2][j]
        if (se == "MAS" or se == "SAM") and (sw == "MAS" or sw == "SAM"):
            return 1
    return 0

found = 0
for i in range(h):
    for j in range(w):
        found += look2(grid, i, j)

print(f"part 2 found : {found}")
