import unittest
from sar_adc import convert

class TestSARADC(unittest.TestCase):
    def test_endpoints(self):
        self.assertEqual(convert(0).code, 0)
        self.assertEqual(convert(3.3).code, 255)

    def test_midscale(self):
        self.assertEqual(convert(1.65).code, 128)

    def test_near_fullscale(self):
        self.assertEqual(convert(3.3 - 0.001).code, 255)

    def test_bit_trace(self):
        result = convert(1.65)
        self.assertEqual(result.bits, (1, 0, 0, 0, 0, 0, 0, 0))
        self.assertEqual(len(result.trial_codes), 8)

    def test_invalid_inputs(self):
        for vin in (-0.1, 3.4):
            with self.assertRaises(ValueError):
                convert(vin)
        with self.assertRaises(ValueError):
            convert(1, bits=0)

if __name__ == "__main__":
    unittest.main()
