def get_person_type(person_age):
    if person_age < 0:
        return "Invalid. You haven't even been born yet."
    if person_age > 125:
        return "Invalid. Gravestone."
    elif person_age <= 1:
        return "Infant."
    elif person_age < 13:
        return "Child."
    elif person_age < 20:
        return "Teenager."
    else: return "Adult."
print(get_person_type(0))
print(get_person_type(2))
print(get_person_type(7))
print(get_person_type(17))
print(get_person_type(42))
print(get_person_type(130))

import unittest

class test_get_person_type(unittest.TestCase):
    def test_infant(self):
        self.assertEqual(get_person_type(3), "Infant.")
    def test_child(self):
        self.assertEqual(get_person_type(5), "Child.")
    def test_teenager(self):
        self.assertEqual(get_person_type(16), "Teenager.")
    def test_adult(self):
        self.assertEqual(get_person_type(34), "Adult.")

if __name__ == '__main__':
    unittest.main()