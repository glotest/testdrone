import unittest

class MyTest(unittest.TestCase):

    def test_add(self):
        self.assertEqual(1 + 3, 4) 

    def test_divide(self):
        self.assertEqual(8 / 2, 5)
        
    def test_foo(self):
        self.assertEqual('foo', 'bar')

if __name__ == '__main__':
    unittest.main()
