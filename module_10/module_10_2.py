from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies = 100

    def run(self):
        print(f'{self.name} на нас напали!')
        days = 0
        while self.enemies > 0:
            sleep(1)
            days += 1
            self.enemies -= self.power
            print(f'{self.name}, сражается {days} день(дня)..., осталось {self.enemies} воинов.')
        print(f'{self.name} одержал победу спустя {days} дня(дней)!')


if __name__ == "__main__":
    first_knight = Knight('Sir Lancelot', 10)
    second_knight = Knight('Sir Galahad', 20)

    first_knight.start()
    second_knight.start()
    first_knight.join()
    second_knight.join()

    print('Все битвы закончились!')
