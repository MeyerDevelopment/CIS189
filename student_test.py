import unittest
from class_definitions_package import student as t

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.student = t.Student('Duck', 'Daisy', 'Comp Sci')

    def tearDown(self):
        del self.student

    def test_initial_value_required_attributes(self):
        self.assertEqual(self.student.last_name, 'Duck')
        self.assertEqual(self.student.first_name, 'Daisy')
        self.assertEqual(self.student.major, 'Comp Sci')

    def test_inital_all_attributes(self):
        student = t.Student('Duck', 'Daisy', 'Comp Sci', 3.9)
        assert student.last_name == 'Duck'
        assert student.first_name == 'Daisy'
        assert student.major == 'Comp Sci'
        assert student.gpa == 3.9

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            p = t.Student('123', 'Daisy', 'Comp Sci')

    def test_object_not_created_error_fist_name(self):
        with self.assertRaises(ValueError):
            p = t.Student('Duck', '123', 'Comp Sci')

    def test_object_not_created_error_major(self):
        with self.assertRaises(ValueError):
            p = t.Student('Duck', 'Daisy', '123')

    def test_object_not_created_error_gpa(self):
        with self.assertRaises(ValueError):
            p = t.Student('Duck', 'Daisy', 'abc', 'r')

    def test_student_str(self):
        self.assertEqual(str(self.student), 'Duck, Daisy has major Comp Sci with gpa: 0.0')


if __name__ == '__main__':
    unittest.main()
