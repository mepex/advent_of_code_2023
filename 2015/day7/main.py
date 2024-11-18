import re

f = "input.txt"

def process_op(v, op):
    if re.search("^\d+$", op):
        return int(op)
    else:
        return v[op]
def process_inst(v, inst):
    s = [x.strip() for x in inst.split("->")]
    if re.search("^\d+$", s[0]):
        v[s[1]] = int(s[0])
        return
    op = s[0].split()
    try:
        if len(op) == 1:
            v[s[1]] = v[op[0]]
            return
        if len(op) == 2:
            v[s[1]] = ~ v[op[1]]
        else:
            if op[1] == "AND":
                v[s[1]] = process_op(v, op[0]) & process_op(v, op[2])
            elif op[1] == "OR":
                v[s[1]] = process_op(v, op[0]) | process_op(v, op[2])
            elif op[1] == "LSHIFT":
                v[s[1]] = process_op(v, op[0]) << process_op(v, op[2])
            elif op[1] == "RSHIFT":
                v[s[1]] = process_op(v, op[0]) >> process_op(v, op[2])
        v[s[1]] = v[s[1]] & 0xFFFF
    except KeyError as e:
        #print(f"not found: {e}")
        return
    except:
        print(f"error on inst: {inst}")
        raise
    print(f"exec {inst.strip()}")


with open(f, 'r') as fp:
    instructions = fp.readlines()

v = {}
# basically process instructions over and over until a appears, make take some iterations
while not 'a' in v.keys():
    for i in instructions:
        process_inst(v, i)

print(v)
print(f"part one: a = {v['a']}")
part1 = v['a']
v = {'b' : part1}
while not 'a' in v.keys():
    for i in instructions:
        process_inst(v, i)

print(v)
print(f"part 2:  a = {v['a']}")


