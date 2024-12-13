import requests
from datetime import datetime
from threading import Thread

THE_URL = 'http://binaryjazz.us/wp-json/genrenator/v1/genre/'


def first():
    res = []
    # Set the start and end date for the API request

    for i in range(6):
        response = requests.get(THE_URL)
        page_response = response.json()
        res.append(page_response)
    print(res)


def second():
    res = []

    def func(url):
        response = requests.get(url)
        page_response = response.json()
        res.append(page_response)

    thr_first = Thread(target=func, args=(THE_URL,))
    thr_second = Thread(target=func, args=(THE_URL,))
    thr_third = Thread(target=func, args=(THE_URL,))
    thr_fourth = Thread(target=func, args=(THE_URL,))
    thr_fifth = Thread(target=func, args=(THE_URL,))
    thr_sixth = Thread(target=func, args=(THE_URL,))

    thr_first.start()
    thr_second.start()
    thr_third.start()
    thr_fourth.start()
    thr_fifth.start()
    thr_sixth.start()

    thr_first.join()
    thr_second.join()
    thr_third.join()
    thr_fourth.join()
    thr_fifth.join()
    thr_sixth.join()
    print(res)


if __name__ == '__main__':
    funcs = [first, second]
    for f in funcs:
        start_time = datetime.now()
        f()
        end_time = datetime.now()
        time_res = end_time - start_time
        print('Execution Time:', time_res)
