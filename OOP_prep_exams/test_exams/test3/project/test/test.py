from project.senior_student import SeniorStudent
from unittest import TestCase,main
class SeniorStudentTest(TestCase):
    def setUp(self):
        self.s = SeniorStudent("TestID","Test",2.0)
    def test_init(self):
        self.s = SeniorStudent("TestID", "Test", 2.0)
        self.assertEqual(self.s.student_id, "TestID")
        self.assertEqual(self.s.name,"Test")
        self.assertEqual(self.s.student_gpa, 2.0)
        self.assertEqual(self.s.colleges, set())
    def test_invalid_student_id(self):
        with self.assertRaises(ValueError) as ex:
            self.s.student_id = "Tes"
        self.assertEqual(str(ex.exception),"Student ID must be at least 4 digits long!")
    def test_valid_student_id(self):
        self.assertEqual(self.s.student_id, "TestID")
    def test_invalid_student_name(self):
        with self.assertRaises(ValueError) as ex:
            self.s.name = ""
        self.assertEqual(str(ex.exception),"Student name cannot be null or empty!")
    def test_invalid_student_GPA(self):
        with self.assertRaises(ValueError) as ex:
            self.s.student_gpa = 0.9
        self.assertEqual(str(ex.exception),"Student GPA must be more than 1.0!")
    def test_invalid_apply_to_college(self):
        result = self.s.apply_to_college(3,"TestC")
        self.assertEqual(result,'Application failed!')
    def test_valid_apply_to_college(self):
        result = self.s.apply_to_college(2,"TestC")
        self.assertEqual(result,f'Test successfully applied to TestC.')
    def test_invalid_update_gpa(self):
        result = self.s.update_gpa(0.9)
        self.assertEqual(result,'The GPA has not been changed!')
    def test_valid_update_gpa(self):
        result = self.s.update_gpa(3)
        self.assertEqual(result,'Student GPA was successfully updated.')
    def test_invalid_eq(self):
        s2 = SeniorStudent("TestID","Test",3.0)
        result = self.s.student_gpa == s2.student_gpa
        self.assertEqual(result, False)
    def test_valid_eq(self):
        s2 = SeniorStudent("TestID", "Test", 2.0)
        result = self.s.student_gpa == s2.student_gpa
        self.assertEqual(result, True)


if __name__ == "__main__":
    main()
