from random import seed, randrange
import sys

try:
    for_seed, length = (int(x) for x in input('Enter two integers, the second '
                                              'one being strictly positive: '
                                              ).split()
                        )
    if length <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(for_seed)
values = [randrange(1, 7) for _ in range(length)]
print('Here are the generated values:', values, '\n')

diff = values[-1] - values[0]
print('The difference between last and first values is:\n  ', diff, '\n')

import numpy as np

a = len(values)
b = max(values)
T = np.zeros(shape=(a, b))
m = 0;
n = 0

while (m < a):
    t = values[m]
    while (n < b):
        if t > 0:
            T[m][n] = 1
            n = n + 1
            t = t - 1
        else:
            T[m][n] = 0
            n = n + 1
            t = t - 1
    m = m + 1;
    n = 0

hori = '\n'
i = 0
while (i < len(values)):
    j = 0
    hori = hori + 4 * ' '
    while (j < max(values)):
        if (T[i][j] > 0):
            hori = hori + ' ' + '*' + ' '
            j = j + 1
        else:
            j = j + 1
    i = i + 1
    hori = hori + '\n'

print('Here are the values represented as horizontal bars:')
print(hori)

a = max(values)
b = len(values)
T = np.zeros(shape=(a, b))

n = 0
while (n < len(values)):
    m = max(values) - 1
    t = values[n]
    while (m >= 0):
        if t > 0:
            T[m][n] = 1
            m = m - 1
            t = t - 1
        else:
            T[m][n] = 0
            m = m - 1
            t = t - 1
    n = n + 1

vert = '\n'
i = 0
while (i < max(values)):
    j = 0
    vert = vert + 3 * ' ' + '|'
    while (j < len(values)):
        if (T[i][j] > 0):
            vert = vert + ' ' + '*' + ' '
            j = j + 1
        else:
            vert = vert + 3 * ' '
            j = j + 1
    i = i + 1
    vert = vert + '|' + '\n'

edge = 3 * ' ' + '-' * (3 * len(values) + 2)
vert = '\n' + edge + vert + edge

print('Here are the values represented as vertical bars, with a surrounding frame:')
print(vert)