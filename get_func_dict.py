import unittest

def get_func_dict(obj):
    # TODO: Construct a dictionary out of the object where:
    #  Keys are function names
    #  Values are the callable functions
    #
    # Ignore private and protected functions (i.e. whose names begin with '_')
    return {}


class GetFuncDictTestCase(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None

    def test_0_functions_2_attributes(self):
        # Given
        class Object:
            foo = 'test'
            bar = 1.5

        obj = Object()

        # When
        actual = get_func_dict(obj)
        expected = {}

        # Then
        self.assertDictEqual(expected, actual)

    def test_2_functions_3_attributes(self):
        # Given
        class Object:
            a = 'text'
            b = 1.5
            c = 2

            def foo(self):
                return self.a * self.c

            def bar(self):
                return self.b * self.c

        obj = Object()

        # When
        actual = get_func_dict(obj)
        expected = {
            'foo': obj.foo,
            'bar': obj.bar,
        }

        # Then
        self.assertDictEqual(expected, actual)
        self.assertEqual('texttext', actual['foo'](), msg="Oops!")
        self.assertEqual(3.0, actual['bar']())

    def test_2_functions_0_attributes(self):
        # Given
        class Object:

            def foo(self):
                return 'texttext'

            def bar(self):
                return 3.0

        obj = Object()

        # When
        actual = get_func_dict(obj)
        expected = {
            'foo': obj.foo,
            'bar': obj.bar,
        }

        # Then
        self.assertDictEqual(expected, actual)
        self.assertEqual('texttext', actual['foo'](), msg="Oops!")
        self.assertEqual(3.0, actual['bar']())

    def test_2_functions_3_attributes_1_private_function_1_protected_function(self):
        # Given
        class Object:
            a = 'text'
            b = 1.5
            c = 2

            def foo(self):
                return self.a * self.c

            def bar(self):
                return self.b * self.c

            def __private(self):
                return "Private"

            def _protected(self):
                return f"Hi, I'm Protected. He's {self.__private()}."

        obj = Object()

        # When
        actual = get_func_dict(obj)
        expected = {
            'foo': obj.foo,
            'bar': obj.bar,
        }

        # Then
        self.assertDictEqual(expected, actual)
        self.assertEqual('texttext', actual['foo']())
        self.assertEqual(3.0, actual['bar']())
        self.assertEqual("Hi, I'm Protected. He's Private.", obj._protected())

    def test_1_private_function_1_protected_function(self):
        # Given
        class Object:
            def __private(self):
                return "Private"

            def _protected(self):
                return f"Hi, I'm Protected. He's {self.__private()}."

        obj = Object()

        # When
        actual = get_func_dict(obj)
        expected = {}

        # Then
        self.assertDictEqual(expected, actual)
        self.assertEqual("Hi, I'm Protected. He's Private.", obj._protected())


suite = unittest.TestLoader().loadTestsFromTestCase(GetFuncDictTestCase)
runner = unittest.TextTestRunner()
runner.run(suite)
