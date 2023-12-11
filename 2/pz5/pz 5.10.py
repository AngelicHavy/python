# Знайти найближче до заданого значення число в заданому масиві:

import numpy as np
Z = np.arange(100)
v = np.random.uniform(0,100)
index = (np.abs(Z-v)).argmin()
print(Z[index])