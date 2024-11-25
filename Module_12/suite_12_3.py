import unittest
import tests_12_3

# Создание TestSuite
suite = unittest.TestSuite()
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

if __name__ == '__main__':
    # Создаем и запускаем TestRunner с verbosity=2
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
