import hashlib

# initializing string
str2hash = "iwrupvqb"

h = 11111
i = 0
while str(h)[:5] != "00000":
    s = str2hash + str(i)
    result = hashlib.md5(s.encode())
    h = result.hexdigest()
    i += 1

print(f"1st part: {s} : {h}")

while str(h)[:6] != "000000":
    s = str2hash + str(i)
    result = hashlib.md5(s.encode())
    h = result.hexdigest()
    i += 1

print(f"2nd part: {s} : {i-1} : {h}")