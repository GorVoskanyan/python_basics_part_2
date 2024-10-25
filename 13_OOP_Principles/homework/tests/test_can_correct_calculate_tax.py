import unittest
# https://docs.python.org/3.12/library/unittest.html#unittest.TestCas


class Property:
    def __init__(self, value):
        self.set_value(value)

    def get_value(self):
        return self._value

    def set_value(self, value):
        if value > 0:
            self._value = value  # protected
        else:
            raise ValueError('Value must be non-negative.')

class Car(Property):
    def __init__(self, value):
        super().__init__(value)

    def calculate_tax(self):
        tax = self._value / 200
        print(f'Tax for Car: {tax:.2f}')
        return tax

class TestPropertyValue(unittest.TestCase):

    def test_can_set_incorrect_type(self):
        with self.assertRaises(TypeError):
            property_obj = Property('abc')

    def test_can_set_negative_value(self):
        ...

    def test_can_get_correct_tax(self):
        car_object = Car(20000)
        tax = car_object.calculate_tax()
        expected_tax = 100
        self.assertEqual(tax, expected_tax)

if __name__ == '__main__':
    unittest.main()