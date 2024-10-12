from time import sleep
from datetime import datetime
from threading import Thread


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='UTF-8') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово № {i}\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


files_dict = {1: 10, 2: 20,
              3: 200, 4: 100,
              5: 10, 6: 30,
              7: 200, 8: 100}

if __name__ == '__main__':
    start_time = datetime.now()
    for key, value in list(files_dict.items())[:4]:
        write_words(value, f'example{key}.txt')

    end_time = datetime.now()
    time_res = end_time - start_time
    print(f'Работа потоков: {time_res}')

    start_time = datetime.now()
    threads = []
    for key, value in list(files_dict.items())[4:]:
        thread = Thread(target=write_words, args=(value, f'example{key}.txt'))
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    end_time = datetime.now()
    time_res = end_time - start_time
    print(f'Работа потоков: {time_res}')
