# Створити масив 10x10 з випадковими значеннями, знайти мінімум і максимум:

import numpy as np
Z = np.random.random((10,10))
Zmin, Zmax = Z.min(), Z.max()
print(Zmin, Zmax)