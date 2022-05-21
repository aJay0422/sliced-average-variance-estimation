# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from save import SAVE
import numpy as np




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    X = np.random.randn(500, 5)
    s1 = X[:,0] + X[:,1] - 2 * X[:,2]
    s2 = X[:,0] - 2 * X[:,1] + X[:,2]
    y = ((s1 * s2) > 0)
    y = y.astype(int)
    save = SAVE(n_slices=2)
    X_save = save.fit_transform(X, y)
    print(save.eigenvalues_)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
