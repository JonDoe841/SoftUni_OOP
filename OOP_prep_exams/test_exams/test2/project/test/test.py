from unittest import TestCase,main
from project.soccer_player import SoccerPlayer
class SoccerPlayerTest(TestCase):
    def setUp(self):
        self.t = SoccerPlayer("test12",18,1,"Barcelona")
    def test_init(self):
        self.assertEqual(self.t.name,"test12")
        self.assertEqual(self.t.age,18)
        self.assertEqual(self.t.goals,1)
        self.assertEqual(self.t.team,"Barcelona")
        self.assertEqual(self.t.achievements,{})
        self.assertEqual(self.t._VALID_TEAMS,["Barcelona", "Real Madrid",
                                              "Manchester United",
                                              "Juventus", "PSG"])

    def test_name_invalid(self):
        with self.assertRaises(ValueError) as ex:
            self.t.name = "t"
        self.assertEqual(str(ex.exception),"Name should be more than 5 symbols!")
    def test_age_invalid(self):
        with self.assertRaises(ValueError) as ex:
            self.t.age = 15
        self.assertEqual(str(ex.exception),"Players must be at least 16 years of age!")
    def test_goal_invalid(self):
        self.t.goals = -15
        self.assertEqual(self.t.goals,0)
    def test_team_invalid(self):
        with self.assertRaises(ValueError) as ex:
            self.t.team = 'Test'
        self.assertEqual(str(ex.exception),f"Team must be one of the following: Barcelona, Real Madrid,"
                                              " Manchester United,"
                                              " Juventus, PSG!")
    def test_change_team_invalid(self):
        result = self.t.change_team("Test")
        self.assertEqual(result,"Invalid team name!")
    def test_change_team_valid(self):
        self.t.team = "Juventus"
        self.assertEqual(self.t.team, "Juventus")
        result = self.t.change_team("PSG")
        self.assertEqual(result,"Team successfully changed!")
        self.assertEqual(self.t.team, "PSG")
    def test_add_new_achievement_not_there(self):
        self.t.achievements = {}
        result = self.t.add_new_achievement("smt")
        self.assertEqual(result,"smt has been successfully added to the achievements collection!")
    def test_add_new_achievement_there(self):
        self.t.achievements = {"smt":0}
        result = self.t.add_new_achievement("smt")
        self.assertEqual(result,"smt has been successfully added to the achievements collection!")
        self.assertEqual(self.t.achievements, {"smt":1})
    def test_lt_p2_better(self):
        p2 = SoccerPlayer("test21", 18, 1, "Barcelona")
        self.t = SoccerPlayer("test12", 18, 0, "Barcelona")
        result = self.t.__lt__(p2)
        self.assertEqual(result,f"test21 is a top goal scorer! S/he scored more than test12.")
    def test_lt_p1_better(self):
        p2 = SoccerPlayer("test21", 18, 0, "Barcelona")
        self.t = SoccerPlayer("test12", 18, 1, "Barcelona")
        result = self.t.__lt__(p2)
        self.assertEqual(result,"test12 is a better goal scorer than test21.")

if __name__ == "__main__":
    main()