from sympy import factorint
from itertools import combinations
import math
from functools import reduce

def factors(n):
    return set(x for tup in ([i, n//i]
                for i in range(1, int(n**0.5)+1) if n % i == 0) for x in tup)

f = factorint(12)
primes = []
for k, v in f.items():
    primes.extend([k] * v)
print(primes)

print(factors(1000000))
print(sum(factors(1000000)))

# looking for first number where all its factors add up to 3310000 or more
gold = 3310000

i = 700000
f = sorted(factors(i))
factor_sum = sum(f)
while factor_sum < gold:
    f = sorted(factors(i))
    factor_sum = sum(f)
    i += 1

print(f"{i} : {factor_sum} : {f}")

presents = 0

i = 500000
while presents < gold * 10:
    f = []
    presents = 0
    fs = factors(i)
    for y in fs:
        if i <= 50 * y:
            f.append(y)
    for x in f:
        presents += x * 11
    if presents < gold * 10:
        i += 1
    else:
        pass

print(f"{i} : presents: {presents}")

