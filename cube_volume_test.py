import unittest
import cube_volume

def test_cube_volume(self):
    result = test_cube_volume.cube(1)
    self.assertEqual(result, 2)

class testCaseCube(unittest.TestCase):
    def test_cube(self):
        self.assertEqual(cube_volume.cube(3), 27)

    def test_cube_02(self):
        self.assertEqual(cube_volume.cube(1), 1)

    def test_cube_03(self):
        self.assertEqual(cube_volume.cube(-1), -1)

    def test_cube_04(self): #fail condition
        self.assertEqual(cube_volume.cube(zero), 0)

if __name__ == '__main__':
    unittest.main()