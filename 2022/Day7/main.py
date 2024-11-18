import re
import copy



def add_entry(entry):
    global fs, current_dir
    # check for dir existence
    toks = current_dir.split("/")

    if len(toks) == 2:
        fs["contents"].append(entry)
        return

    d = fs["contents"]
    for t in toks:
        for e in d:
            if e["name"] == t and e["type"] == "dir":
                d = e["contents"]
                continue
    d.append(entry)


def add_dir(dirname):
    global fs, current_dir
    # check for dir existence
    toks = current_dir.split("/")
    entry = {"name": dirname, "type": "dir", "size": 0, "contents": []}

    if len(toks) == 2:
        fs["contents"].append(entry)
        return

    d = fs["contents"]
    for t in toks:
        for e in d:
            if e["name"] == t and e["type"] == "dir":
                d = e["contents"]
                continue
    d.append(entry)

def add_file(filename, size):
    global fs, current_dir
    # check for dir existence
    toks = current_dir.split("/")
    entry = {"name": filename, "type": "file", "size": size}
    if len(toks) == 2:
        fs["contents"].append(entry)
        return

    d = fs["contents"]
    # first and last entries will be '' because current_dir always starts and ends with /
    for t in toks[1:-1]:
        for e in d:
            if e["name"] == t and e["type"] == "dir":
                d = e["contents"]
                continue
    d.append(entry)

def _finditem(obj, key):
    if obj["name"] == key:
        return obj
    for k, v in obj.items():
        if isinstance(v,dict):
            item = _finditem(v, key)
            if item is not None:
                return item
        elif isinstance(v,list):
            for list_item in v:
                item = _finditem(list_item, key)
                if item is not None:
                    return item


def finditem(obj, key):
    if obj["name"] == key:
        return obj
    for k, v in obj.items():
        if isinstance(v,dict):
            item = finditem(v, key)
            if item is not None:
                return item
        else:
            print("not dict!: {v")

def iterdict(d):
  for k,v in d.items():
     if isinstance(v, dict):
         iterdict(v)
     else:
         print (k,":",v)

def get_current_dir() -> list:
    global fs, current_dir
    # check for file existence
    toks = current_dir.split("/")[1:]
    d = fs["contents"]
    if toks[0] == "":
        return d
    for t in toks:
        for e in d:
            if e["name"] == t and e["type"] == "dir":
                d = e["contents"]
    return d

def recalculate_sizes(d) -> int:
    sum = 0
    for e in d["contents"]:
        if e["type"] == "file":
            sum += e["size"]
        else:
            s = recalculate_sizes(e)
            e["size"] = s
            sum += s
    return sum

def find_threshold(threshold, d) -> int:
    sum = 0
    for e in d["contents"]:
        if e["type"] == "file":
            pass
        else:
            sum += find_threshold(threshold, e)
            if e["size"] <= threshold:
                sum += e["size"]
                print(f"{e['name']} : {e['size']}")
    return sum

def find_dir(threshold, d) -> int:
    best = 1e20
    for e in d["contents"]:
        if e["type"] == "file":
            pass
        else:
            if e["size"] > threshold:
                r = find_dir(threshold, e)
                best = min(best, r, e["size"])
                print(f"{best} {e['size']} {r}")
    return best




# print list of dictionaries with indentation
def print_structure(d, indent = ''):
    if d["type"] == "dir":
        print(f"{indent}- {d['name']} ({d['type']}, total size = {d['size']})")
        indent += "  "
        for f in d["contents"]:
            print_structure(f, indent)
    else:
        print(f"{indent}- {d['name']} ({d['type']}, size = {d['size']})")



# filesystem
# data structure: keys are the name of files or dirs
# if file, the val is the size.  If dir, the value is a dict.
# {
#   name: "/",
#   type: "dir",
#   contents: [
#   {
#       name: "filename1",
#       type: "file",
#       size: 123
#   },
#   {
#       name: "subdir1",
#       type: "dir",
#       size: 234,
#       contents: [
#           {
#               name: "subdir2"
#               type: "dir",
#               size: 0,
#               contents: {}
#           },
#           {
#               name: "file2"
#               type: "file"
#               size: 345
#           },
#       ]
#   }
#   ]
# }
#
#
#
# }
#
fs = {
    "name": "/",
    "type": "dir",
    "size": 0,
    "contents": []
}

current_dir = "/"

ls_output = False

with open("input.txt") as fp:
    lines = [line.strip() for line in fp]

for i in range(len(lines)):
    line = lines[i]
    match = re.match(r"\$ (\w+) *([A-Za-z0-9./]*)", line)
    if match:
        cmd = match.group(1)
        arg = match.group(2)
        if cmd == 'cd':
            if arg == "/":
                current_dir = "/"
            elif arg == "..":
                toks = current_dir.split("/")
                current_dir = "/".join(toks[:-2]) + "/"
            else:
                current_dir += arg + "/"
            ls_output = False
        if cmd == 'ls':
            ls_output = True
    else:
        match = re.match(r"(\d+) ([A-Za-z0-9.]+)", line)
        if match:
            size = int(match.group(1))
            filename = match.group(2)
            add_entry({"name": filename, "type": "file", "size": size, "contents": []})
        else:
            match = re.match(r"dir ([A-Za-z0-9.]+)", line)
            if match:
                dirname = match.group(1)
                add_entry({"name": dirname, "type": "dir", "size": 0, "contents": []})
            else:
                print(f"ERROR: bad ls output {line}")
    i += 1

#print_structure(fs)
total_size = recalculate_sizes(fs)
fs["size"] = total_size
print_structure(fs)
answer = find_threshold(100000, fs)
print(f"answer to part one: {answer}")

total_fs_size = fs["size"]
total_space = 70000000
update_space_needed = 30000000
free_space = total_space - total_fs_size
needed = update_space_needed - free_space
print(f"total file size: {total_fs_size}, space to clear for update: {needed}")

# find dir that is larger and closest to 30000000

# 13683830
# 1609574
answer = find_dir(needed, fs)
print(f"answer to part two: {answer}")



