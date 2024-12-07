import runner
import unittest


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.all_result = {}

    def setUp(self) -> None:
        self.Usain = runner.Runner('Усэйн', 10)
        self.Andrey = runner.Runner('Андрей', 9)
        self.Nick = runner.Runner('Ник', 3)

    def test_tournament1(self):
        self.tournament = runner.Tournament(90, self.Usain, self.Nick)
        self.all_result = self.tournament.start()
        self.assertTrue(self.all_result.get(max(self.all_result.keys())) == "Ник")
        TournamentTest.all_result[0] = self.all_result

    def test_tournament2(self):
        self.tournament = runner.Tournament(90, self.Andrey, self.Nick)
        self.all_result = self.tournament.start()
        self.assertTrue(self.all_result.get(max(self.all_result.keys())) == "Ник")
        TournamentTest.all_result[1] = self.all_result

    def test_tournament3(self):
        self.tournament = runner.Tournament(90, self.Usain, self.Andrey, self.Nick)
        self.all_result = self.tournament.start()
        self.assertTrue(self.all_result.get(max(self.all_result.keys())) == "Ник")
        TournamentTest.all_result[2] = self.all_result

    def test_tournament4(self):
        self.tournament = runner.Tournament(5, self.Usain, self.Andrey, self.Nick)
        self.all_result = self.tournament.start()
        self.assertTrue(self.all_result.get(max(self.all_result.keys())) == "Ник")
        TournamentTest.all_result[3] = self.all_result

    @classmethod
    def tearDownClass(cls) -> None:
        for result in TournamentTest.all_result.values():
            show_result = {}
            for key, runner in result.items():
                show_result[key] = runner.name
            print(show_result)


if __name__ == "__main__":
    unittest.main()
