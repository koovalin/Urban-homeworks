import os
import time

directory = os.getcwd()


def get_files_info(parent_dir):
    for root, dirs, files in os.walk(parent_dir):
        for file in files:
            filepath = os.path.join(root, file)
            filetime = os.path.getmtime(filepath)
            formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
            filesize = os.path.getsize(filepath)
            parent_dir = os.path.basename(root)

            print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт,'
                  f'Время изменения: {formatted_time}, Родительская директория: {parent_dir}')


if __name__ == '__main__':
    get_files_info(directory)
