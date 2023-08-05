import pandas as pd
import matplotlib.pyplot as plt
import math


mult_grid = []


def is_prime(number):
    if number <= 1:
        return False

    for counter in range(2,  int(math.sqrt(number)) + 1):
        if number % counter == 0:
            return False
    return True


def print_grid(collisions):
    for row in collisions:
        print(row)


for count_y in range(2, 101):
    mults = []
    count_x = 1
    mult = count_x * count_y
    while mult < 100:
        mults.append(mult)
        count_x += 1
        mult = count_x * count_y
    mult_grid.append(mults)

mults_concat = []
for row in mult_grid:
    mults_concat += row

print_grid(mult_grid)
print()
print(mults_concat)

mults_concat_count = {}
for mult in mults_concat:
    if mult in mults_concat_count:
        mults_concat_count[mult] += 1
    else:
        mults_concat_count[mult] = 1

print(mults_concat_count)

hits = []
for count in range(1, 100):
    if count in mults_concat_count:
        hits.append(mults_concat_count[count])
    else:
        hits.append(0)

print(hits)

df = pd.DataFrame({'hits': hits})
df.plot.bar()
plt.show()



