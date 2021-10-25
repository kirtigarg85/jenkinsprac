import cuboid_volume 
import unittest
class TestCuboid(unittest.TestCase):
    def test_volume(self):
        self.assertAlmostEqual(cuboid_volume.volume(2),8)
        self.assertAlmostEqual(cuboid_volume.volume(1),1)
        self.assertAlmostEqual(cuboid_volume.volume(0),0)
        self.assertAlmostEqual(cuboid_volume.volume(5.5),166.375)
    def test_input_value(self):
        self.assertRaises(TypeError,cuboid_volume,True)

if __name__=="__main__":
    unittest.main()
