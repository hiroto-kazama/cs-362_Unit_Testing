import unittest
import name_gen 

class testCaseName(unittest.TestCase):
    def test_name(self):
        self.assertEqual(name_gen.full_name('Hiroto', 'Kazama'), "Hiroto Kazama")

    def test_name_02(self):
        self.assertEqual(name_gen.full_name('123', '123'), "123 123")

    def test_name_03(self):
        self.assertEqual(name_gen.full_name('', ''), " ")

    def test_name_04(self):#fail condition
        self.assertEqual(name_gen.full_name(''), " ")

if __name__ == '__main__':
    unittest.main()