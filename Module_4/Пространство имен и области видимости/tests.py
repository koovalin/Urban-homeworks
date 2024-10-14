import sortfunc as sf
import time, inspect
from my_array import int_array


def start_test_all_functions(module, runs=100):
    def func_test_time(func, runs):
        def avg_(a): return sum(a) / len(a) * 100

        av = []
        for _ in range(runs):
            start = time.process_time()
            func(int_array)
            finish = time.process_time()
            res_msec = finish - start
            av.append(res_msec)
        return avg_(av)

    def func_test(func):
        print(f'Время работы {str(func.__name__)}: {func_test_time(func, runs)}')

    functions = inspect.getmembers(module, inspect.isfunction)
    for func in functions:
        func_test(func[1])


if __name__ == '__main__':
    start_test_all_functions(sf, 50)
