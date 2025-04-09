from unittest import TestCase,main
from project.climbing_robot import ClimbingRobot

class ClimbingRobotTest(TestCase):
    def setUp(self):
        self.c = ClimbingRobot("Mountain",
                               "idk",10,100)
    def test_init(self):
        self.assertEqual(self.c.ALLOWED_CATEGORIES,['Mountain', 'Alpine', 'Indoor', 'Bouldering'])
        self.assertEqual(self.c.category, "Mountain")
        self.assertEqual(self.c.part_type,"idk")
        self.assertEqual(self.c.capacity,10)
        self.assertEqual(self.c.memory,100)
        self.assertEqual(self.c.installed_software,[])
    def test_invalid_category(self):
        with self.assertRaises(ValueError) as ex:
            self.c.category = "Test"
        self.assertEqual(str(ex.exception),f"Category should be one of ['Mountain', 'Alpine', 'Indoor', 'Bouldering']")
    def test_get_used_capacity(self):
        result = self.c.get_used_capacity()
        self.assertEqual(result, 0)
        self.c.installed_software = [{"name":'Test',"capacity_consumption":10,"memory_consumption":10}]
        result = self.c.get_used_capacity()
        self.assertEqual(result, 10)
    def test_get_available_capacity(self):
        self.c.installed_software = [{"name":'Test',"capacity_consumption":10,"memory_consumption":10}]
        result = self.c.get_available_capacity()
        self.assertEqual(result,0)
        self.c.capacity = 100
        result = self.c.get_available_capacity()
        self.assertEqual(result, 90)
    def test_get_used_memory(self):
        result = self.c.get_used_memory()
        self.assertEqual(result,0)
        self.c.installed_software = [{"name": 'Test', "capacity_consumption": 10, "memory_consumption": 100}]
        result = self.c.get_used_memory()
        self.assertEqual(result, 100)
    def test_get_available_memory(self):
        result = self.c.get_available_memory()
        self.assertEqual(result,100)
    def test_invalid_install_software(self):
        result = self.c.install_software( {"name": 'Test', "capacity_consumption": 10, "memory_consumption": 101})
        self.assertEqual(result,"Software 'Test' cannot be installed on Mountain part.")
    def test_valid_install_software(self):
        result = self.c.install_software( {"name": 'Test', "capacity_consumption": 10, "memory_consumption": 10})
        self.assertEqual(result,f"Software 'Test' successfully installed on Mountain part.")
if __name__ == "__main__":
    main()