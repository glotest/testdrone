import unittest

class MyTest(unittest.TestCase):

    def test_add(self):
        self.assertEqual(1 + 3, 4) 

if __name__ == '__main__':
    unittest.main()