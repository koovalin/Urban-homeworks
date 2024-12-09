import unittest
import logging

logging.basicConfig(
    level=logging.INFO,
    filemode='w',
    filename='runner_tests.log',
    encoding='UTF-8',
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def skip_if_frozen(method):
    """Декоратор для пропуска тестов, если атрибут is_frozen установлен в True."""

    def wrapper(self, *args, **kwargs):
        if getattr(self, 'is_frozen', False):
            self.skipTest('Тесты в этом кейсе заморожены')
        else:
            return method(self, *args, **kwargs)

    return wrapper


class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class RunnerTest(unittest.TestCase):
    is_frozen = False

    def setUp(self):
        self.runner = Runner("Тестовый", speed=5)

    @skip_if_frozen
    def test_challenge(self):
        self.assertEqual(self.runner.speed, 5)

    @skip_if_frozen
    def test_run(self):
        try:
            runner = Runner(1234, speed=5)
            runner.run()
            self.assertEqual(self.runner.distance, 10)
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning(f'Неверная скорость для Runner: {e}')

    @skip_if_frozen
    def test_walk(self):
        try:
            runner = Runner("Тест", speed=-5)
            runner.walk()
            self.assertEqual(self.runner.distance, 5)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning(f'Неверная скорость для Runner: {e}')


class TournamentTest(unittest.TestCase):
    is_frozen = True

    def setUp(self):
        self.Usain = Runner("Усэйн", speed=10)
        self.Andrey = Runner("Андрей", speed=9)
        self.Nick = Runner("Ник", speed=3)

    @skip_if_frozen
    def test_first_tournament(self):
        # Пример теста турнира
        tournament = Tournament(90, self.Usain, self.Nick)
        results = tournament.start()
        self.assertEqual(str(results[1]), "Усэйн")

    @skip_if_frozen
    def test_second_tournament(self):
        # Пример теста турнира
        tournament = Tournament(90, self.Andrey, self.Nick)
        results = tournament.start()
        self.assertEqual(str(results[1]), "Андрей")

    @skip_if_frozen
    def test_third_tournament(self):
        # Пример теста турнира
        tournament = Tournament(90, self.Usain, self.Andrey, self.Nick)
        results = tournament.start()
        self.assertEqual(str(results[1]), "Усэйн")


if __name__ == "__main__":
    unittest.main()