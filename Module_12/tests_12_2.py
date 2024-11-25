import unittest
from pprint import pprint


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
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


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.Usain = Runner("Усэйн", speed=10)
        self.Andrey = Runner("Андрей", speed=9)
        self.Nick = Runner("Ник", speed=3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            printable_result = {place: str(runner) for place, runner in result.items()}
            print(printable_result)

    def test_race_Usain_Nick(self):
        tournament = Tournament(90, self.Usain, self.Nick)
        results = tournament.start()
        self.__class__.all_results['Usain_Nick'] = results
        self.assertTrue(results[max(results)] == "Ник")

    def test_race_Andrey_Nick(self):
        tournament = Tournament(90, self.Andrey, self.Nick)
        results = tournament.start()
        self.__class__.all_results['Andrey_Nick'] = results
        self.assertTrue(results[max(results)] == "Ник")

    def test_race_Usain_Andrey_Nick(self):
        tournament = Tournament(90, self.Usain, self.Andrey, self.Nick)
        results = tournament.start()
        self.__class__.all_results['Usain_Andrey_Nick'] = results
        self.assertTrue(results[max(results)] == "Ник")


if __name__ == "__main__":
    unittest.main()
