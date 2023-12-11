# Дано масив 10x2 (точки в декартовій системі координат), перетворити в полярну:

import numpy as np
Z = np.random.random((10,2))
X, Y = Z[:,0], Z[:,1]
R = np.hypot(X, Y)
T = np.arctan2(Y, X)
print(R)
print(T)