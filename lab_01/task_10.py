"""Задание 10 (1 балл): Напишите функцию, которая принимает на вход абсолютный путь к
директории и две строки с расширениями файлов. В результате её выполнения у всех файлов
в указанной директории,имеющих первое расширение, расширение должно измениться на второе.
 В конце работы функция должна возвращать кортеж из двух элементов:
1. сколько всего в директории файлов (именно файлов, не директорий);
2. у скольки из них расширение было изменено."""

import os
import fnmatch


def task_10_func(dir_path, prev_extension, next_extension):
    """

        функция принимает путь к папке
        и типы файлов. Возвращет количество
        файлов и файлов с измененным раширением.
        """
    total = 0
    changed = 0
    for fname in os.listdir(dir_path):
        total += 1
        if fnmatch.fnmatch(fname, '*.tx_'):
            pre, tx_ = os.path.splitext(fname)
            os.rename(fname, pre + '.txt')
            changed += 1

    return total, changed


if __name__ == "__main__":
    prev_extension = 'tx_'
    next_extension = 'txt'
    dir_path = os.chdir(r'dir_root')
    total, changed = task_10_func(dir_path, prev_extension, next_extension)
    print('Всего в директории:', total)
    print('Расширение было изменено:', changed)
