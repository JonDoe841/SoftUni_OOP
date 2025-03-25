from project.gallery import Gallery
from unittest import TestCase,main
class GalleryTest(TestCase):
    def setUp(self):
        self.g = Gallery("Test",
                         "Sofia",
                         15.5,
                         True)
    def test_init(self):
        g = Gallery("Test",
                        "Sofia",
                        15.5,
                        True)
        self.assertEqual(g.gallery_name, "Test")
        self.assertEqual(g.city, "Sofia")
        self.assertEqual(g.area_sq_m, 15.5)
        self.assertEqual(g.open_to_public, True)
    def test_invalid_gname(self):
        with self.assertRaises(ValueError) as ex:
            self.g.gallery_name = "Test!"
        self.assertEqual(str(ex.exception),"Gallery name can contain letters and digits only!")
    def test_invalid_city_name(self):
        with self.assertRaises(ValueError) as ex:
            self.g.city = "1Test"
        self.assertEqual(str(ex.exception),"City name must start with a letter!")
    def test_invalid_area_sq_m(self):
        with self.assertRaises(ValueError) as ex:
            self.g.area_sq_m = -1
        self.assertEqual(str(ex.exception),"Gallery area must be a positive number!")
    def test_already_added_exhibition(self):
        self.g.add_exhibition("Test1", 17)
        result = self.g.add_exhibition("Test1", 17)
        self.assertEqual(result,f'Exhibition "Test1" already exists.')
    def test_valid_add_exhibition(self):
        result = self.g.add_exhibition("Test1", 17)
        self.assertEqual(result, f'Exhibition "Test1" added for the year 17.')
    def test_invalid_remove_exhibition(self):
        result = self.g.remove_exhibition("Test2")
        self.assertEqual(result,f'Exhibition "Test2" not found.')
    def test_valid_remove_exhibition(self):
        self.g.add_exhibition("Test1", 17)
        result = self.g.remove_exhibition("Test1")
        self.assertEqual(result,'Exhibition "Test1" removed.')
    def test_valid_list_exhibitions(self):
        self.g.add_exhibition("Test1", 18)
        result = self.g.list_exhibitions()
        self.assertEqual(result,f"Test1: 18")
    def test_invalid_list_exhibitions(self):
        self.g.open_to_public = False
        result = self.g.list_exhibitions()
        self.assertEqual(result, f"Gallery Test is currently closed for public! Check for updates later on.")
if __name__ == "__main__":
    main()