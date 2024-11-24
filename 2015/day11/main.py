import re

def increment_pw(s):
    if s == '':
        return 'a'
    elif s[-1] == 'z':
        return increment_pw(s[:-1]) + 'a'
    else:
        return s[:-1] + chr(ord(s[-1]) + 1)

pw = ["aaa", "xy", "xz", "xzz", "xzzzzzz", "zz"]

for p in pw:
    print(f"{p} +1 = {increment_pw(p)}")

def find_straight(s):
    for i in range(len(s)-3):
        if ord(s[i]) + 1 == ord(s[i+1]) and ord(s[i+1]) + 1 == ord(s[i+2]):
            return True
    return False

def check_pw(pw):
    if re.findall("[iol]", pw):
        return False
    m = re.findall(r"(.)\1{1,}", pw)
    if not m or len(m) < 2:
        return False
    return find_straight(pw)

pw = "hepxcrrq"

while not check_pw(pw):
    pw = increment_pw(pw)
    #print(f"next: {pw}")

print(f"answer part 1: {pw}")

pw = increment_pw(pw)

while not check_pw(pw):
    pw = increment_pw(pw)

print(f"answer part 1: {pw}")
