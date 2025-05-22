import unittest
import math
from calculator import allowed_names

class TestCalculator(unittest.TestCase):
    def test_log(self):
        # Test valid inputs
        self.assertAlmostEqual(eval("log(math.e)", {"__builtins__": {}, "math": math}, allowed_names), 1.0)
        self.assertAlmostEqual(eval("log(10)", {"__builtins__": {}, "math": math}, allowed_names), math.log(10))
        
        # Test edge cases
        self.assertAlmostEqual(eval("log(1)", {"__builtins__": {}, "math": math}, allowed_names), 0.0)
        
        # Test invalid inputs
        with self.assertRaises(ValueError):
            eval("log(0)", {"__builtins__": {}, "math": math}, allowed_names)
        with self.assertRaises(ValueError):
            eval("log(-1)", {"__builtins__": {}, "math": math}, allowed_names)

    def test_log10(self):
        # Test valid inputs
        self.assertAlmostEqual(eval("log10(100)", {"__builtins__": {}, "math": math}, allowed_names), 2.0)
        self.assertAlmostEqual(eval("log10(1000)", {"__builtins__": {}, "math": math}, allowed_names), 3.0)
        
        # Test edge cases
        self.assertAlmostEqual(eval("log10(1)", {"__builtins__": {}, "math": math}, allowed_names), 0.0)
        
        # Test invalid inputs
        with self.assertRaises(ValueError):
            eval("log10(0)", {"__builtins__": {}, "math": math}, allowed_names)
        with self.assertRaises(ValueError):
            eval("log10(-1)", {"__builtins__": {}, "math": math}, allowed_names)

if __name__ == '__main__':
    unittest.main()
