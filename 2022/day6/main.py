# a set can only have unique values, so add the potential start of packet to a set and see
# if the lengths are equal
def is_sop(s):
  myset = set(s)
  return True if len(myset) == len(s) else False

buf = ''
i = 0
with open("input.txt") as f:
  while True:
    c = f.read(1)
    if not c:
      print("End of file")
      break
    i += 1
    buf += c
    if len(buf) > 4:
      buf = buf[1:]
    if len(buf) < 4:
      continue
    if is_sop(buf):
      break

print(f"SOP starts at {i} : {buf}")

i = 0
with open("input.txt") as f:
  while True:
    c = f.read(1)
    if not c:
      print("End of file")
      break
    i += 1
    buf += c
    if len(buf) > 14:
      buf = buf[1:]
    if len(buf) < 14:
      continue
    if is_sop(buf):
      break

print(f"SOP starts at {i} : {buf}")