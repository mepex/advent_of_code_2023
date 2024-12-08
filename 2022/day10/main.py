import re


x_vals = []
x = 1
with open("input.txt") as fp:
    for line in fp:
        if line.strip() == "noop":
            x_vals.append(x)
            print(f"{len(x_vals)} : noop clock : {x_vals[-1]}")
        else:
            match = re.match(r"addx ([-0-9]+)", line.strip())
            if match:
                add = int(match.group(1))
                x_vals.append(x)
                print(f"{len(x_vals)} : addx {add} clock1  : {x_vals[-1]}")
                x += add
                x_vals.append(x)
                print(f"{len(x_vals)} : addx {add} clock2 : {x_vals[-1]}")


sum = 0
for i in range(18, 220, 40):
    sum += (i + 2) * x_vals[i]
    print(f"x at {i} : {x_vals[i]} .... {sum}")

print(f"sum: {sum}\n\n\n\n")

x_vals = []
x = 1
crt = []
cycle = 1
with open("input.txt") as fp:
    for line in fp:
        pixel = (cycle-1) % 40
        if line.strip() == "noop":
            x_vals.append(x)
            if abs(pixel - x) < 2:
                ch = "#"
            else:
                ch = "."
            crt.append(ch)
            print(f"{cycle} ({pixel}): noop\t: {x_vals[-1]}\t {''.join(crt)}")
        else:
            match = re.match(r"addx ([-0-9]+)", line.strip())
            if match:
                add = int(match.group(1))
                if abs(pixel - x) < 2:
                    ch = "#"
                else:
                    ch = "."
                crt.append(ch)
                x_vals.append(x)
                print(f"{cycle} ({pixel}): a{add}\t: {x_vals[-1]}\t {''.join(crt)}")
                cycle += 1
                pixel = (cycle-1) % 40
                if abs(pixel - x) < 2:
                    ch = "#"
                else:
                    ch = "."
                crt.append(ch)
                x += add
                x_vals.append(x)
                print(f"{cycle} ({pixel}): a{add}]\t: {x_vals[-1]}\t {''.join(crt)}")
        cycle += 1

print("".join(crt[0:40]))
print("".join(crt[40:80]))
print("".join(crt[80:120]))
print("".join(crt[120:160]))
print("".join(crt[160:200]))
print("".join(crt[200:240]))


