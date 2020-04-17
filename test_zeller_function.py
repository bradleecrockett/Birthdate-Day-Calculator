from unittest import TestCase
from BdayCalc import zeller_function

class TestZeller_function(TestCase):

    def test_zeller_function1(self):
        self.assertEqual(zeller_function(1, 1, 2000), "Saturday")

    def test_zeller_function2(self):
        self.assertEqual(zeller_function(2, 14, 2021), "Sunday")

    def test_zeller_function3(self):
        self.assertEqual(zeller_function(3, 10, 1984), "Saturday")

    def test_zeller_function4(self):
        self.assertEqual(zeller_function(4, 16, 2020), "Thursday")

    def test_zeller_function5(self):
        self.assertEqual(zeller_function(5, 5, 1850), "Sunday")

    def test_zeller_function6(self):
        self.assertEqual(zeller_function(3, 10, 1984), "Saturday")

    def test_zeller_function7(self):
        self.assertEqual(zeller_function(7, 4, 1792), "Wednesday")

    def test_zeller_function8(self):
        self.assertEqual(zeller_function(8, 10, 2020), "Monday")

    def test_zeller_function9(self):
        self.assertEqual(zeller_function(9, 11, 2001), "Tuesday")

    def test_zeller_function10(self):
        self.assertEqual(zeller_function(10, 31, 2020), "Saturday")

    def test_zeller_function11(self):
        self.assertEqual(zeller_function(11, 20, 1900), "Tuesday")

    def test_zeller_function12(self):
        self.assertEqual(zeller_function(12, 31, 1999), "Friday")

