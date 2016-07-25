import unittest
import lib

class HanoiTestCase(unittest.TestCase):

    def test_hanoi(self):
        self.assertListEqual(
            hanoi(2, ['a', 'b', 'c']),
            [("a","c"), ("a","b"), ("c","b")]
        )

    def test_is_valid(self):
        self.assertTrue(isValid([0, 1]))


if __name__ == '__main__':
    unittest.main()
