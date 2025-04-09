from project.restaurant import Restaurant
from unittest import TestCase,main
class RestaurantTest(TestCase):
    def setUp(self):
        self.r = Restaurant("Test", 20)
    def test_init(self):
        self.assertEqual(self.r.name, "Test")
        self.assertEqual(self.r.capacity,20)
        self.assertEqual(self.r.waiters, [])
    def test_invalid_name(self):
        with self.assertRaises(ValueError) as ex:
            self.r.name = ""
        self.assertEqual(str(ex.exception), "Invalid name!")
        with self.assertRaises(ValueError) as ex:
            self.r.name = "     "
        self.assertEqual(str(ex.exception), "Invalid name!")
    def test_invalid_capacity(self):
        with self.assertRaises(ValueError)as ex:
            self.r.capacity = -1
        self.assertEqual(str(ex.exception),"Invalid capacity!")
    def test_invalid_get_waiters(self):
        self.r.waiters = [{"name": "Test", "total_earnings": 100}, {"name": "Test1"}]
        result = self.r.get_waiters()
        self.assertEqual(result,[{"name": "Test", "total_earnings": 100}, {"name": "Test1"}])
    def test_invalid_add_waiter_no_room(self):
        self.r.waiters = [1,2]
        self.r.capacity = 2
        result = self.r.add_waiter("Test1")
        self.assertEqual(result,"No more places!")
    def test_invalid_add_waiter_already_in(self):
        self.r.waiters = [{"name": "Test"}]
        result = self.r.add_waiter("Test")
        self.assertEqual(result,"The waiter Test already exists!")
    def test_valid_add_waiter(self):
        self.r.waiters = [{"name": "Test"}]
        result = self.r.add_waiter("Test1")
        self.assertEqual(result,f"The waiter Test1 has been added.")
        self.assertEqual(self.r.waiters,[{"name": "Test"},{"name": "Test1"}])
    def test_invalid_remove_waiter(self):
        self.r.waiters = [{"name": "Test"}]
        result = self.r.remove_waiter("Test1")
        self.assertEqual(result,f"No waiter found with the name Test1.")
    def test_valid_remove_waiter(self):
        self.r.waiters = [{"name": "Test"}]
        result = self.r.remove_waiter("Test")
        self.assertEqual(result, f"The waiter Test has been removed.")
        self.assertEqual(self.r.waiters, [])
    def test_get_total_earnings_when_nothing(self):
        result = self.r.get_total_earnings()
        self.assertEqual(result,0)
    def test_get_total_earnings_when_smt(self):
        self.r.waiters = [{"name": "Test","total_earnings":100},{"name": "Test1"}]
        result = self.r.get_total_earnings()
        self.assertEqual(result,100)

if __name__ == "__main__":
    main()