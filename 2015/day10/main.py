s = ["1113222113"]

runs = 51

i = 0
while i < runs:
    prev_ch = ""
    count = 1
    st = str(s[-1])
    desc = ""
    for ch in st:
        if ch == prev_ch:
            count += 1
        elif prev_ch != '':
            desc += f"{count}{prev_ch}"
            count = 1
        prev_ch = ch
    if count == 1:
        desc += f"1{ch}"
    else:
        desc += f"{count}{prev_ch}"
    s.append(str(desc))
    i+= 1

for i in range(runs):
    print(f"{i} : {len(s[i])}")
