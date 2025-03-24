from Lesson8_Testing.List.List import IntegerList
from unittest import TestCase, main

class TestIntegerList(TestCase):
    def setUp(self):
        self.cl = IntegerList(1,2,3)
    def test_ini_int_values(self):
        self.assertListEqual([1,2,3],self.cl._IntegerList__data)

    def test_init_non_integers_are_skipped(self):
        new_list = IntegerList("asd", 4.8, [1,2,3], 5)
        self.assertListEqual([5], new_list._IntegerList__data)

    def test_get_data_return_private__data(self):
        result = self.cl.get_data()

        self.assertListEqual([1,2,3], result)
        self.assertIs(self.cl._IntegerList__data, result)

    def test_add_non_integer_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.cl.add("asd")
            self.cl.add(4.5)
            self.cl.add([1,2,3])
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_add_integer(self):
        self.assertListEqual([1,2,3], self.cl._IntegerList__data)

        result = self.cl.add(5)
        self.assertListEqual([1, 2, 3, 5], self.cl._IntegerList__data)

        self.assertIs(self.cl._IntegerList__data,result)

    def test_remove_invalid(self):
        lenght = len(self.cl._IntegerList__data)
        with self.assertRaises(IndexError)as ex:
            self.cl.remove_index(lenght)
            lenght +=1
            self.cl.remove_index(lenght)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_remove_index(self):
        self.assertListEqual([1, 2, 3], self.cl._IntegerList__data)
        result = self.cl.remove_index(1)
        self.assertEqual(2, result)
        self.assertListEqual([1,3],self.cl._IntegerList__data)
        self.assertNotIn(2,self.cl._IntegerList__data)

    def test_get_invalid(self):
        lenght = len(self.cl._IntegerList__data)
        with self.assertRaises(IndexError) as ex:
            self.cl.get(lenght)
            lenght += 1
            self.cl.get(lenght)
        self.assertEqual("Index is out of range", str(ex.exception))
    def test_get_el(self):
        self.assertListEqual([1, 2, 3], self.cl._IntegerList__data)
        result = self.cl.get(1)
        self.assertEqual(2,result)
        self.assertListEqual([1,2,3],self.cl._IntegerList__data)

    def test_invalid_index_insert_raise(self):
        lenght = len(self.cl._IntegerList__data)
        with self.assertRaises(IndexError) as ex:
            self.cl.insert(lenght,5)
            lenght += 1
            self.cl.get(lenght)
    def test_invalid_el(self):
        el = "asd"
        with self.assertRaises(IndexError) as ex:
            self.cl.insert(0,el)
            el += 3.5
            self.cl.insert(0,el)
            el = [1,2,4]
            self.cl.insert(0, el)
        self.assertEqual("Element is not Integer",str(ex.exception))

    def test_insert(self):
        self.assertListEqual([1,2,3],self.cl._IntegerList__data)
        result = self.cl.insert(0,5)
        self.assertIsNone(result)
        self.assertListEqual([5,1,2,3], self.cl._IntegerList__data)
    def test_get_biggest(self):
        new_list = IntegerList(3,-2,100,8)
        result = new_list.get_biggest()
        self.assertEqual(100,result)
    def test_get_ind(self):
        self.assertIn(1, self.cl._IntegerList__data)
        self.assertEqual(1, self.cl._IntegerList__data[0])

        result = self.cl.get_index(1)
        self.assertEqual(0, result)

if __name__ == "__main__":
    main()


