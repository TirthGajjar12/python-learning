import unittest

# def addNumbers(a,b):
#     return a+b

# class TestMathsfunction(unittest.TestCase):

#     def test_add_Numbers(self):
#         self.assertEqual(addNumbers(10,5),15)
#         self.assertEqual(addNumbers(-1,1),0)
#         self.assertEqual(addNumbers(0,0),0)


# if __name__ == "__main__":
#     unittest.main()



#practice 1 

# def is_even(number):
#     return number % 2 == 0

# class TestMathsfunc(unittest.TestCase):
#     def testdivideNUmber(self):
#         self.assertTrue(is_even(4))
#         self.assertFalse(is_even(7))

# if __name__ == "__main__":
#     unittest.main()


#practice 2 


# def format_name(firstname,lastname):
#     return f"{firstname.capitalize()} {lastname.capitalize()}"


# class test_case(unittest.TestCase):
#     def test_iscapitalizeornot(self):
#         self.assertEqual(format_name("jhone","DOE"),"Jhone Doe")
#         self.assertEqual(format_name("jane", "smith"),"Jane Smith")

# if __name__ == "__main__":
#     unittest.main()

#pracices 3

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

class test_cases(unittest.TestCase):
    def test_for_division(self):
        self.assertRaises(ValueError,divide,10,0)
        # self.assertEqual(divide(10,0),0)


if __name__ == "__main__":
    unittest.main()

    