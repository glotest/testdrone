import unittest

class MyTest(unittest.TestCase):
    def setUp(self):
        self.auth=S3Auth(ACCESS_KEY, SECRET_KEY)
    
    def test_add(self):
        self.assertEqual(1 + 3, 4) 