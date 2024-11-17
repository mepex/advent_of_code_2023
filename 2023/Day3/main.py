import re



idx = 0
part_nums = []
symbols = []

with open("input.txt") as fp:
    for line in fp:
        result = re.finditer(r"(\d+)", line.strip())
        for r in result:
            part_no = int(r.group())
            (start, end) = r.span()
            part_nums.append((idx, start, end, part_no))
        result = re.finditer(f"[^\.0-9]", line.strip())
        for r in result:
            symbol = r.group()
            (start, end) = r.span()
            symbols.append((idx, start, end, symbol))
        idx = idx + 1

print(part_nums)
print(symbols)

sum = 0
for s_line, s_start, s_end, s in symbols:
    for p_line, p_start, p_end, p in part_nums:
        # same line
        if p_line in range(s_line - 1, s_line + 2):
            if s_start in range(p_start, p_end + 1) or s_end in range(p_start, p_end + 1):
                sum = sum + p
                print(f"Found {p} at ({p_line}, {p_start}, {p_end})")

print(f"part 1 sum is {sum}")

sum = 0
for s_line, s_start, s_end, s in symbols:
    if s == "*":
        nums = []
        for p_line, p_start, p_end, p in part_nums:
            if p_line in range(s_line - 1, s_line + 2):
                if s_start in range(p_start, p_end + 1) or s_end in range(p_start, p_end + 1):
                    nums.append(p)
        if len(nums) == 2:
            ratio = nums[0] * nums[1]
            print(f"Found {nums} near ({s_line}, {s_start}, {s_end})")
            sum = sum + ratio

print(f"part 2 sum is {sum}")




