import unittest

from shipping.package import Package, Stacks

class TestPackage(unittest.TestCase):
    def setUp(self):
        # Standard package with all dimensions and weight within limits
        self.standard_package = Package(10, 10, 10, 10)

        # Bulky volume package with volume greater than MAX_VOLUME
        self.bulky_volume_package = Package(
            Package.MAX_DIMENSION - 1,
            Package.MAX_DIMENSION - 1,
            Package.MAX_DIMENSION - 1,
            10,
        )

        # Bulky dimension package with any dimension greater than MAX_DIMENSION
        # while volume is within limits
        self.bulky_dimension_package = Package(
            Package.MAX_DIMENSION, 10, 10, 10
        )

        # Heavy package with weight greater than MAX_WEIGHT while volume and
        # dimensions are within limits
        self.heavy_package = Package(10, 10, 10, Package.MAX_WEIGHT)

        # Rejected package is bulky and heavy
        self.rejected_package = Package(
            Package.MAX_DIMENSION,
            Package.MAX_DIMENSION,
            Package.MAX_DIMENSION,
            Package.MAX_WEIGHT,
        )

    def test_volume_calculation(self):
        expected_volume = 10 * 10 * 10
        self.assertEqual(self.standard_package.get_volume(), expected_volume)

    def test_bulky_check(self):
        self.assertFalse(self.standard_package.is_bulky())
        self.assertTrue(self.bulky_volume_package.is_bulky())
        self.assertTrue(self.bulky_dimension_package.is_bulky())
        self.assertTrue(self.rejected_package.is_bulky())

    def test_oversized_check(self):
        self.assertFalse(self.standard_package.is_oversized())
        self.assertFalse(self.bulky_volume_package.is_oversized())
        self.assertTrue(self.bulky_dimension_package.is_oversized())
        self.assertTrue(self.rejected_package.is_oversized())

    def test_sort(self):
        print(self.standard_package.sort())
        self.assertEqual(self.standard_package.sort(), Stacks.STANDARD.value)
        self.assertEqual(self.bulky_volume_package.sort(), Stacks.SPECIAL.value)
        self.assertEqual(self.bulky_dimension_package.sort(), Stacks.SPECIAL.value)
        self.assertEqual(self.rejected_package.sort(), Stacks.REJECTED.value)


if __name__ == "__main__":
    unittest.main()
