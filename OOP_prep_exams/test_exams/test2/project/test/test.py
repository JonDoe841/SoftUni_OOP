from project.soccer_player import SoccerPlayer
from unittest import TestCase, main

class SoccerPlayerTests(TestCase):
    def setUp(self):
        self.p = SoccerPlayer("TestTest", 18, 1,"Barcelona")
    #TODO if _VALID_TEAMS does get checked
    def test_init(self):
        p = SoccerPlayer("TestTest", 18, 2,"Barcelona")
        self.assertEqual(p.name, "TestTest")
        self.assertEqual(p.age, 18)
        self.assertEqual(p.goals, 2)
        self.assertEqual(p.team, "Barcelona")
        self.assertEqual(p.achievements, {})
    def test_name_invalid(self):
        with self.assertRaises(ValueError) as ex:
            self.p.name = "Test5"
        self.assertEqual(str(ex.exception), "Name should be more than 5 symbols!")
        with self.assertRaises(ValueError) as ex:
            self.p.name = "Test"
        self.assertEqual(str(ex.exception), "Name should be more than 5 symbols!")
    def test_invalid_age(self):
        with self.assertRaises(ValueError) as ex:
            self.p.age = 15
        self.assertEqual(str(ex.exception),"Players must be at least 16 years of age!")
    def test_negative_goals(self):
        self.p.goals = -1
        self.assertEqual(self.p.goals, 0)
    def test_invalid_team(self):

        with self.assertRaises(ValueError) as ex:
            self.p.team = "Test"
        self.assertEqual(str(ex.exception),f"Team must be one of the following: {', '.join(SoccerPlayer._VALID_TEAMS)}!")
    def test_invalid_change_team(self):
        self.assertEqual(self.p.team, "Barcelona")
        result = self.p.change_team("Test")
        self.assertEqual(result,"Invalid team name!")
        self.assertEqual(self.p.team, "Barcelona")
    def test_valid_change_team(self):
        self.assertEqual(self.p.team, "Barcelona")
        result = self.p.change_team("Juventus")
        self.assertEqual(result, "Team successfully changed!")
        self.assertEqual(self.p.team, "Juventus")
    def test_invalid_achievement(self):
        self.assertEqual(self.p.achievements, {})
        result = self.p.add_new_achievement("Test")
        self.assertEqual(result,f"Test has been successfully added to the achievements collection!")
        self.assertEqual(self.p.achievements, {"Test": 1})
        result = self.p.add_new_achievement("Test")
        self.assertEqual(result, f"Test has been successfully added to the achievements collection!")
        self.assertEqual(self.p.achievements, {"Test": 2})
        result = self.p.add_new_achievement("Test2")
        self.assertEqual(result, f"Test2 has been successfully added to the achievements collection!")
        self.assertEqual(self.p.achievements, {"Test": 2, "Test2": 1})
    def test_comparison(self):
        p2 = SoccerPlayer("Test21", 19, 1,"Juventus")
        result = self.p < p2
        self.assertEqual(result,f"{self.p.name} is a better goal scorer than {p2.name}.")
        p2.goals =2
        result = p2 < self.p
        self.assertEqual(result, f"{p2.name} is a better goal scorer than {self.p.name}.")
        self.p.goals = 1
        self.assertLess(self.p.goals,p2.goals)
        result = self.p < p2
        self.assertEqual(result, f"{p2.name} is a top goal scorer! S/he scored more than {self.p.name}.")

if __name__ == "__main__":
    main()