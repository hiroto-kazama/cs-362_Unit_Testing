import unittest
import avg_elem 

class testCase(unittest.TestCase):
    def test_avg(self):
        Var = avg_elem.cal_average([1, 2, 3])
        self.assertEqual(Var, 2)

    def test_avg_02(self):
        Var = avg_elem.cal_average([])
        self.assertEqual(Var, 0)

    def test_avg_03(self):
        Var = avg_elem.cal_average([-1, 0, 1])
        self.assertEqual(Var, 0)

if __name__ == '__main__':
    unittest.main()