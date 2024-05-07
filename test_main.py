import unittest
from the_volume_of_the_shapes import calculate_volume

class FlaskTest(unittest.TestCase):
    #def setUp(self):
    #    self.app = app.test_client()
    
    def test_cube_volume(self):
        params = {'side_length': '3'}
        precision = 2
        volume = calculate_volume('cube', params, precision)
        self.assertEqual(volume, 27.0)
    
    def test_sphere_volume(self):
        params = {'radius': '2'}
        precision = 2
        volume = calculate_volume('sphere', params, precision)
        self.assertAlmostEqual(volume, 33.51, places=2)
    
    def test_cylinder_volume(self):
        params = {'radius': '2', 'height': '4'}
        precision = 2
        volume = calculate_volume('cylinder', params, precision)
        self.assertAlmostEqual(volume, 50.27, places=2)
    
    def test_invalid_shape(self):
        params = {'side_length': '3'}
        precision = 2
        volume = calculate_volume('invalid_shape', params, precision)
        self.assertIsNone(volume)