import numpy as np

a = np.array([[255,2,3],[255,255,6]])

a_ = np.where(a != 255)

a = a[a_]
print(a)