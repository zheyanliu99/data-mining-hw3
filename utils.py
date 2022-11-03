# %%
import numpy as np
from scipy.stats import chi2
def random_normal_with_chi(size, chi_value):
    size0 = 0
    size1 = 0
    x_list = []
    y_list = []
    while size0 + size1 < size[0]:
        x = np.random.normal(0, 1, size[1])
        y = 1 if np.sum(x**2) > chi_value else 0
        if y == 0 and size0 < size[0]/2:
            size0 += 1
            x_list.append(x)
            y_list.append(y)
        elif y == 1 and size1 < size[0]/2:
            size1 += 1
            x_list.append(x)
            y_list.append(y)
    X = np.concatenate(x_list, axis = 0).reshape(size[0], 10)
    y = np.array(y_list)
    return X, y
            
X, y = random_normal_with_chi((10, 10), chi2.ppf(q=0.5, df=10))
# %%
