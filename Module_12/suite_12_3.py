import unittest
from tests_12_2 import Runner, Tournament


def skip_if_frozen(method):
    """Декоратор для пропуска тестов, если атрибут is_frozen установлен в True."""
    def wrapper(self, *args, **kwargs):
        if getattr(self, 'is_frozen', False):
            self.skipTest('Тесты в этом кейсе заморожены')
        else:
            return method(self, *args, **kwargs)
    return wrapper


class RunnerTest(unittest.TestCase):
    is_frozen = False

    def setUp(self):
        # Подготовка к тесту Runner (пример)
        self.runner = Runner("Тестовый", speed=5)

    @skip_if_frozen
    def test_challenge(self):
        # Пример теста
        self.assertEqual(self.runner.speed, 5)

    @skip_if_frozen
    def test_run(self):
        # Пример теста
        self.runner.run()
        self.assertEqual(self.runner.distance, 10)

    @skip_if_frozen
    def test_walk(self):
        # Пример теста
        self.runner.walk()
        self.assertEqual(self.runner.distance, 5)


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


# Создание TestSuite
suite = unittest.TestSuite()
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))


if __name__ == '__main__':
    # Создаем и запускаем TestRunner с verbosity=2
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
