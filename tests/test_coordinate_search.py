import unittest
from src.coordinate_search import minimize


class CoordinateSearchTests(unittest.TestCase):
    def test_quadratic(self):
        point, value = minimize(lambda p: (p[0] - 2) ** 2 + (p[1] + 1) ** 2,
                                [0.0, 0.0], tolerance=1e-4)
        self.assertAlmostEqual(point[0], 2.0, delta=0.02)
        self.assertAlmostEqual(point[1], -1.0, delta=0.02)
        self.assertLess(value, 1e-3)

    def test_rejects_empty_start(self):
        with self.assertRaises(ValueError):
            minimize(lambda p: 0, [])


if __name__ == "__main__":
    unittest.main()
