import unittest
from tmc import points
from tmc.utils import load, load_module, run_test

@points('part01-02')
class SevenBrothersTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_module('src.seven_brothers', 'en')

    def test_output(self):
        output = run_test(self.module)
        expected = ["Aapo", "Eero", "Juhani", "Lauri", "Simeoni", "Timo", "Tuomas"]
        
        for idx, name in enumerate(expected):
            self.assertEqual(output[idx], name, f"The output at line {idx+1} should be {name}, but it was {output[idx] if idx < len(output) else 'missing'}")

if __name__ == '__main__':
    unittest.main()


    