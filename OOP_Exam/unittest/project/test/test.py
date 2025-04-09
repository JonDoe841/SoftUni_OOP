from unittest import TestCase, main
from project.star_system import StarSystem
class StarSystemTest(TestCase):
    def setUp(self):
        self.s = StarSystem("Test",
                            "Red giant",
                            "Single",
                            5,
                            (2,3))
    def test_init(self):
        self.assertEqual(self.s.name,"Test")
        self.assertEqual(self.s.star_type,"Red giant")
        self.assertEqual(self.s.system_type, "Single")
        self.assertEqual(self.s.num_planets, 5)
        self.assertEqual(self.s.habitable_zone_range, (2,3))
        self.assertEqual(self.s._STAR_TYPES,{'Red giant', 'Blue giant', 'Yellow dwarf', 'Red dwarf', 'Brown dwarf'})
        self.assertEqual(self.s._STAR_SYSTEM_TYPES,{'Single', 'Binary', 'Triple', 'Multiple'})
    def test_name_invalid(self):
        with self.assertRaises(ValueError) as ex:
            self.s.name = "  "
        self.assertEqual(str(ex.exception),"Name must be a non-empty string.")
    def test_star_type_invalid(self):
        with self.assertRaises(ValueError) as ex:
            self.s.star_type = "Type"
        self.assertEqual(str(ex.exception), "Star type must be one of ['Blue giant', 'Brown dwarf', 'Red dwarf', 'Red giant', 'Yellow dwarf'].")
    def test_system_type_invalid(self):
        with self.assertRaises(ValueError) as ex:
            self.s.system_type = "Type"
        self.assertEqual(str(ex.exception),"System type must be one of ['Binary', 'Multiple', 'Single', 'Triple'].")
    def test_num_planets_invalid(self):
        with self.assertRaises(ValueError) as ex:
            self.s.num_planets = -1
        self.assertEqual(str(ex.exception), "Number of planets must be a non-negative integer.")
    def test_habitable_zone_invalid_size(self):
        with self.assertRaises(ValueError) as ex:
            self.s.habitable_zone_range = (5,1,1)
        self.assertEqual(str(ex.exception),"Habitable zone range must be a tuple of two numbers (start, end) where start < end.")
    def test_habitable_zone_invalid_bigger(self):
        with self.assertRaises(ValueError) as ex:
            self.s.habitable_zone_range = (5,1)
        self.assertEqual(str(ex.exception),"Habitable zone range must be a tuple of two numbers (start, end) where start < end.")
    def test_gt_invalid(self):
        s2 = StarSystem("Test", "Red giant", "Single",
                        0,
                        (2, 3))
        with self.assertRaises(ValueError) as ex:
            result = self.s.__gt__(s2)
        self.assertEqual(str(ex.exception),"Comparison not possible: One or both systems lack a defined habitable zone or planets.")
    def test_gt_valid(self):
        s2 = StarSystem("Test", "Red giant", "Single",
                        1,
                        (2, 5))
        result = self.s.__gt__(s2)
        self.assertEqual(result,False)
    def test_compare_sys_s1_bigger(self):
        s1 = StarSystem("Test1", "Red giant", "Single",
                        1,
                        (5, 10))
        s2 = StarSystem("Test2", "Red giant", "Single",
                        1,
                        (2, 5))
        result = self.s.compare_star_systems(s1,s2)
        self.assertEqual(result,"Test1 has a wider habitable zone than Test2.")
    def test_compare_sys_s2_bigger(self):
        s1 = StarSystem("Test1", "Red giant", "Single",
                        1,
                        (1, 2))
        s2 = StarSystem("Test2", "Red giant", "Single",
                        1,
                        (2, 5))
        result = self.s.compare_star_systems(s1,s2)
        self.assertEqual(result,"Test2 has a wider or equal habitable zone compared to Test1.")
    def test_compare_sys_s2_equal(self):
        s1 = StarSystem("Test1", "Red giant", "Single",
                        1,
                        (1, 2))
        s2 = StarSystem("Test2", "Red giant", "Single",
                        1,
                        (1, 2))
        result = self.s.compare_star_systems(s1,s2)
        self.assertEqual(result,"Test2 has a wider or equal habitable zone compared to Test1.")




if __name__ == "__main__":
    main()

