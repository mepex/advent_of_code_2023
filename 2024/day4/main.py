f = ("sample.txt")
total = 0
grid = []
with open(f) as fp:
    for line in fp:
        line = line.strip()
        grid.append(line)

h = len(grid)
w = len(grid[0])


def look_dir(grid, i, j, m, inc):
    """
    Looks for a string in a grid of characters, any direction is safe because Index
    :param grid: array of strings
    :param i: starting index for y
    :param j: starting index for x
    :param m: string to look for
    :param inc: a tuple that indicates the direction to look e.g (0,1) means look to the right, (-1,-1)
    means look up and to the left
    :return: 1 if found, 0 otherwise
    """
    my_i = i
    my_j = j
    try:
        l = ''
        for x in range(len(m)):
            if my_i < 0 or my_j < 0:
                raise IndexError
            l += grid[my_i][my_j]
            my_i += inc[0]
            my_j += inc[1]
        if l == m:
            return 1
    except IndexError:
        return 0
    return 0

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
        print(f"{i},{j} east: {look_dir(grid, i, j, 'XMAS', (0, 1))}")
        print(f"{i},{j} west: {look_dir(grid, i, j, 'XMAS', (0, -1))}")
        print(f"{i},{j} north: {look_dir(grid, i, j, 'XMAS', (-1, 0))}")
        print(f"{i},{j} south: {look_dir(grid, i, j, 'XMAS', (1, 0))}")
        print(f"{i},{j} southeast: {look_dir(grid, i, j, 'XMAS', (1, 1))}")
        print(f"{i},{j} southwest: {look_dir(grid, i, j, 'XMAS', (1,-1))}")
        print(f"{i},{j} northeast: {look_dir(grid, i, j, 'XMAS', (-1, 1))}")
        print(f"{i},{j} northwest: {look_dir(grid, i, j, 'XMAS', (-1, -1))}")

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
