from unittest import TestCase, main
from project.gallery import Gallery

class GalleryTest(TestCase):
    def setUp(self):
        self.g = Gallery("Test","Sofia",
                    3.14,True)
    def test_init(self):
        self.assertEqual(self.g.gallery_name,"Test")
        self.assertEqual(self.g.city,"Sofia")
        self.assertEqual(self.g.area_sq_m, 3.14)
        self.assertEqual(self.g.open_to_public, True)
        self.assertEqual(self.g.exhibitions,{})
    def test_gallery_name_invalid(self):
        with self.assertRaises(ValueError) as ex:
            self.g.gallery_name = "Test!"
        self.assertEqual(str(ex.exception),"Gallery name can contain letters and digits only!")
    def test_gallery_name_valid(self):
        self.g.gallery_name = "Test    "
        self.assertEqual(self.g.gallery_name,"Test")
    def test_city_invalid_as_num(self):
        with self.assertRaises(ValueError) as ex:
            self.g.city = "3Sofia"
        self.assertEqual(str(ex.exception),"City name must start with a letter!")
    def test_city_invalid_as_symbol(self):
        with self.assertRaises(ValueError) as ex:
            self.g.city = "@Sofia"
        self.assertEqual(str(ex.exception),"City name must start with a letter!")
    def test_city_invalid_as_space(self):
        with self.assertRaises(ValueError) as ex:
            self.g.city = " Sofia"
        self.assertEqual(str(ex.exception),"City name must start with a letter!")
    def test_area_sq_m_invalid(self):
        with self.assertRaises(ValueError) as ex:
            self.g.area_sq_m = -1
        self.assertEqual(str(ex.exception),"Gallery area must be a positive number!")
    def test_add_exhibition_invalid(self):
        self.g.exhibitions = {"smt":2000}
        result = self.g.add_exhibition("smt",2000)
        self.assertEqual(result,'Exhibition "smt" already exists.')
    def test_add_exhibition_valid(self):
        self.g.exhibitions = {"smt":2000}
        self.assertEqual(self.g.exhibitions,{"smt":2000})
        result = self.g.add_exhibition("smt1",2000)
        self.assertEqual(result,'Exhibition "smt1" added for the year 2000.')
        self.assertEqual(self.g.exhibitions,{"smt":2000,"smt1":2000})
    def test_remove_exhibition_invalid(self):
        self.g.exhibitions = {"smt": 2000}
        self.assertEqual(self.g.exhibitions, {"smt": 2000})
        result = self.g.remove_exhibition("smt1")
        self.assertEqual(result,'Exhibition "smt1" not found.')
        self.assertEqual(self.g.exhibitions, {"smt": 2000})

    def test_remove_exhibition_valid(self):
        self.g.exhibitions = {"smt1": 2000}
        self.assertEqual(self.g.exhibitions, {"smt1": 2000})
        result = self.g.remove_exhibition("smt1")
        self.assertEqual(result, 'Exhibition "smt1" removed.')
        self.assertEqual(self.g.exhibitions, {})
    def test_list_exhibitions_false(self):
        self.g.open_to_public = False
        result = self.g.list_exhibitions()
        self.assertEqual(result,'Gallery Test is currently closed for public! Check for updates later on.')
    def test_list_exhibitions_true(self):
        self.g.exhibitions = {"smt": 2000, "smt1": 2000}
        self.g.open_to_public = True
        result = self.g.list_exhibitions()
        self.assertEqual(result,"smt: 2000\nsmt1: 2000")

if __name__ == "__main__":
    main()