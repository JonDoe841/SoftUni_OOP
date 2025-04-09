from collections import deque
from unittest import TestCase, main
from project.railway_station import RailwayStation

class RailwayStationTest(TestCase):
    def setUp(self):
        self.r = RailwayStation("Test")
    def test_init(self):
        self.assertEqual(self.r.name, "Test")
        self.assertEqual(self.r.arrival_trains,deque([]))
        self.assertEqual(self.r.departure_trains,deque([]))
    def test_invalid_name(self):
        with self.assertRaises(ValueError) as ex:
            self.r.name = "Tes"
        self.assertEqual(str(ex.exception), "Name should be more than 3 symbols!")
    def test_new_invalid_on_board(self):
        self.assertEqual(self.r.arrival_trains,deque([]))
        self.r.new_arrival_on_board("idktwin")
        self.assertEqual(self.r.arrival_trains, deque(["idktwin"]))
    def test_invalid_train_has_arrived(self):
        self.r.new_arrival_on_board("idktwin")
        result = self.r.train_has_arrived("idktwin1")
        self.assertEqual(result, "There are other trains to arrive before idktwin1.")
    def test_valid_train_has_arrived(self):
        self.r.new_arrival_on_board("idktwin")
        result = self.r.train_has_arrived("idktwin")
        self.assertEqual(result, "idktwin is on the platform and will leave in 5 minutes.")
        self.assertEqual(self.r.departure_trains,deque(["idktwin"]))
    def test_invalid_train_has_left(self):
        self.r.new_arrival_on_board("idktwin")
        result = self.r.train_has_arrived("idktwin")
        result1 =self.r.train_has_left("idktwin")

        self.assertEqual(result1,True)
    def test_valid_train_has_left(self):
        self.r.new_arrival_on_board("idktwin")
        result = self.r.train_has_arrived("idktwin1")
        result1 = self.r.train_has_left("idktwin")

        self.assertEqual(result1, False)


if __name__ == "__main__":
    main()
