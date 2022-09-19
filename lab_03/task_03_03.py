'''Задание 3 (1 балл): Для векторов V и v построить вектор, в котором на 0-й позиции будет находиться
сумма первых v[0] элементов вектора V, на 1-й - следующих v[1] элементов, и т.д. Гарантируется,
что элементов в V достаточное количество. Пример: для массивов V=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] и
v=[2, 1, 3] ответом будет [3, 3, 15].'''

import numpy as np


def task_3(V, v):
    if len(v) == 0:
        return []
    v_ = np.add.accumulate(v)
    V_ = np.add.accumulate(np.hstack([[0], V]))
    v__ = np.hstack([np.array([0]), v_[:-1]])
    return V_[v_] - V_[v__]

if __name__ == "__main__":

    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    arr_1 = np.array([2, 1, 3])
    result=task_3(arr, arr_1)
    print(list(result))
