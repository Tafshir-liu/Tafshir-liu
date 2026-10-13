import math
import unittest
from power import line_current, three_phase_power

class TestPower(unittest.TestCase):
    def test_unity_pf(self):
        r = three_phase_power(400, 10, 1)
        self.assertAlmostEqual(r["active_w"], math.sqrt(3)*400*10)
        self.assertAlmostEqual(r["reactive_var_magnitude"], 0)

    def test_pf_point_eight(self):
        r = three_phase_power(400, 10, 0.8)
        self.assertAlmostEqual(r["active_w"], r["apparent_va"]*0.8)
        self.assertAlmostEqual(r["reactive_var_magnitude"], r["apparent_va"]*0.6)

    def test_inverse(self):
        self.assertAlmostEqual(line_current(10000, 400, .8), 10000/(math.sqrt(3)*400*.8))

    def test_invalid(self):
        with self.assertRaises(ValueError):
            three_phase_power(400, 10, 1.2)
        with self.assertRaises(ValueError):
            line_current(1000, 400, 0)

if __name__ == "__main__":
    unittest.main()
