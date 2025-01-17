import multiprocessing
from time import time


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)


# Задаем список названий файлов
filenames = [f'./file {number}.txt' for number in range(1, 5)]


def linear_reading():
    start_time = time()
    for filename in filenames:
        read_info(filename)
    duration = time() - start_time
    print(f"Линейный: {duration:.6f} секунд")


def parallel_reading():
    start_time = time()
    with multiprocessing.Pool() as pool:
        pool.map(read_info, filenames)
    duration = time() - start_time
    print(f"Многопроцессный: {duration:.6f} секунд")


if __name__ == '__main__':
    linear_reading()
    parallel_reading()
