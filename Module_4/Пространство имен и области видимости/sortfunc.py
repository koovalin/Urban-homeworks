import inspect


def bubble(array):
    sorted_arr = array.copy()
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(sorted_arr) - 1):
            if sorted_arr[i] > sorted_arr[i + 1]:
                sorted_arr[i], sorted_arr[i + 1] = sorted_arr[i + 1], sorted_arr[i]
                swapped = True
    return sorted_arr


def optimized_bubble(sorted_list):
    number_of_changes = False
    for index in range(len(sorted_list) - 1):
        if sorted_list[index] > sorted_list[index + 1]:
            sorted_list[index], sorted_list[index + 1] = sorted_list[index + 1], sorted_list[index]  # swap
            number_of_changes = True
    if number_of_changes:
        return bubble(sorted_list[:-1]) + [sorted_list[-1]]
    return sorted_list


def selection_sort(array):
    sorted_arr = array.copy()
    for i in range(len(sorted_arr)):
        min_idx = i
        for j in range(i + 1, len(sorted_arr)):
            if sorted_arr[j] < sorted_arr[min_idx]:
                min_idx = j
        sorted_arr[i], sorted_arr[min_idx] = sorted_arr[min_idx], sorted_arr[i]
    return sorted_arr


def insertion_sort(array):
    sorted_arr = array.copy()
    for i in range(1, len(sorted_arr)):
        key = sorted_arr[i]
        j = i - 1
        while j >= 0 and sorted_arr[j] > key:
            sorted_arr[j + 1] = sorted_arr[j]
            j -= 1
        sorted_arr[j + 1] = key
    return sorted_arr


def quick_sort(array):
    sorted_arr = array.copy()
    if len(sorted_arr) <= 1:
        return sorted_arr
    pivot = sorted_arr[len(sorted_arr) // 2]
    left = [x for x in sorted_arr if x < pivot]
    middle = [x for x in sorted_arr if x == pivot]
    right = [x for x in sorted_arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def shell_sort(array):
    sorted_arr = array.copy()
    n = len(sorted_arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = sorted_arr[i]
            j = i
            while j >= gap and sorted_arr[j - gap] > temp:
                sorted_arr[j] = sorted_arr[j - gap]
                j -= gap
            sorted_arr[j] = temp
        gap //= 2
    return sorted_arr
