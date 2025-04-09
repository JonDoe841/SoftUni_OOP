from project.furniture import Furniture
from unittest import TestCase, main
class FurnitureTest(TestCase):
    def setUp(self):
        self.f = Furniture("Test",3.5,
                           (4,3,4),
                           True,
                           3.0)
    def test_init(self):
        self.assertEqual(self.f.model, "Test")
        self.assertEqual(self.f.price, 3.5)
        self.assertEqual(self.f.dimensions, (4,3,4))
        self.assertEqual(self.f.in_stock, True)
        self.assertEqual(self.f.weight, 3.0)
        #tests out if its none since its optional to be float
        self.f.weight = None
        self.assertEqual(self.f.weight, None)
    def test_invalid_model(self):
        with self.assertRaises(ValueError) as ex:
            self.f.model = ""
        self.assertEqual(str(ex.exception), "Model must be a non-empty string with a maximum length of 50 characters.")
        with self.assertRaises(ValueError) as ex:
            #hopefully its 51 note: its 62
            self.f.model = "12345678910123456789101234567891012345678910123456789101"
        self.assertEqual(str(ex.exception), "Model must be a non-empty string with a maximum length of 50 characters.")
    def test_invalid_price(self):
        with self.assertRaises(ValueError) as ex:
            self.f.price = -1
        self.assertEqual(str(ex.exception), "Price must be a non-negative number.")
    def test_invalid_dimensions_of_size_of_tuple(self):
        with self.assertRaises(ValueError) as ex:
            self.f.dimensions = (3,3,3,3)
        self.assertEqual(str(ex.exception),"Dimensions tuple must contain 3 integers.")
    def test_invalid_dimensions_being_negative_in_tuple(self):
        with self.assertRaises(ValueError) as ex:
            self.f.dimensions = (-1,-1,-1)
        self.assertEqual(str(ex.exception),"Dimensions tuple must contain integers greater than zero.")
    def test_invalid_weight(self):
        with self.assertRaises(ValueError) as ex:
            self.f.weight = -1
        self.assertEqual(str(ex.exception),"Weight must be greater than zero.")
    def test_get_available_status_True(self):
        result = self.f.get_available_status()

        self.assertEqual(result, (f"Model: Test is currently "
                f"in stock."))
    def test_get_available_status_False(self):
        self.f.in_stock = False
        result = self.f.get_available_status()
        self.assertEqual(result,f"Model: Test is currently "
                f"unavailable.")
    def test_get_specification_if_weight_is_none(self):
        self.f.weight = None
        result = self.f.get_specifications()
        self.assertEqual(result,(f"Model: Test has the following dimensions: "
                f"4mm x 3mm x 4mm and weighs: N/A"))

    def test_get_specification_if_weight_is_smt(self):
        self.f.weight = 3.0
        result = self.f.get_specifications()
        self.assertEqual(result, (f"Model: Test has the following dimensions: "
                                  f"4mm x 3mm x 4mm and weighs: 3.0"))
if __name__ == "__main__":
    main()
