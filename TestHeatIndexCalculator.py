# TestHeatIndexCalculator.py

# What are we testing for?

# Wide range of inputs
    # - proper and improper
# Boundary Conditions
# Correct outputs
# Test for exceptions

# Import Statements
import unittest
import HeatIndexCalculator

class KnownValues(unittest.TestCase):
    # Formula for unittest method is:
    # test_functionName_testDescription

    def test_calculateHeatIndex_forLowWind_WarmTemp(self):
        # Capture the results of the function
        result = HeatIndexCalculator.calculateHeatIndex(5, 40)
        # Check for expected output
        self.assertEqual(36, result)

    def test_calculateHeatIndex_forLowWind_LowTemp(self):
        result = HeatIndexCalculator.calculateHeatIndex(5, 0)
        expected = -11
        self.assertEqual(expected, result)

    # Add minimum of 5 more unittests
    def test_calculateHeatIndex_forLowWind_ExtremeLowTemp(self):
        result = HeatIndexCalculator.calculateHeatIndex(5, -45)
        expected = -63
        self.assertEqual(expected, result)

    def test_calculateHeatIndex_forMedWind_WarmTemp(self):
        result = HeatIndexCalculator.calculateHeatIndex(35, 40)
        expected = 28
        self.assertEqual(expected, result)

    def test_calculateHeatIndex_forMedWind_LowTemp(self):
        result = HeatIndexCalculator.calculateHeatIndex(40, 0)
        expected = -29
        self.assertEqual(expected, result)

    def test_calculateHeatIndex_forMedWind_ExtremeTemp(self):
        result = HeatIndexCalculator.calculateHeatIndex(45, -45)
        expected = -93
        self.assertEqual(expected, result)

    def test_calculateHeatIndex_forHighWind_WarmTemp(self):
        result = HeatIndexCalculator.calculateHeatIndex(60, 35)
        expected = 17
        self.assertEqual(expected, result)

    def test_calculateHeatIndex_forHighWind_LowTemp(self):
        result = HeatIndexCalculator.calculateHeatIndex(55, -5)
        expected = -39
        self.assertEqual(expected, result)

    def test_calculateHeatIndex_forHighWind_ExtremeTemp(self):
        result = HeatIndexCalculator.calculateHeatIndex(55, -40)
        expected = -97
        self.assertEqual(expected, result)


# Run the tests
if __name__ == '__main__':
    unittest.main()
