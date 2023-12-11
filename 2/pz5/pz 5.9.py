# Замінити максимальний елемент на нуль:

import numpy as np
Z = np.random.random(10)
Z[Z.argmax()] = 0
print(Z)