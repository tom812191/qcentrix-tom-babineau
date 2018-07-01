import unittest

from max_product import max_product, max_product_fast


class TestMaxProduct(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(max_product(None), None)
        self.assertEqual(max_product([]), None)
        self.assertEqual(max_product(()), None)

    def test_invalid(self):
        with self.assertRaises(TypeError):
            max_product(0)

        with self.assertRaises(TypeError):
            max_product({'key': 0})

    def test_short_length(self):
        self.assertEqual(max_product([0]), 0)
        self.assertEqual(max_product([1]), 1)
        self.assertEqual(max_product((0,)), 0)
        self.assertEqual(max_product((1,)), 1)
        self.assertEqual(max_product([-1]), -1)
        self.assertEqual(max_product([1, 0]), 1 * 0)
        self.assertEqual(max_product([5, 5]), 5 * 5)
        self.assertEqual(max_product([-5, 5]), -5 * 5)
        self.assertEqual(max_product((1, 0)), 1 * 0)
        self.assertEqual(max_product((5, 5)), 5 * 5)
        self.assertEqual(max_product((-5, 5)), -5 * 5)
        self.assertEqual(max_product([-5, 5, 1]), -5 * 5 * 1)
        self.assertEqual(max_product([5, 5, 1]), 5 * 5 * 1)
        self.assertEqual(max_product((-5, 5, 1)), -5 * 5 * 1)
        self.assertEqual(max_product((5, 5, 1)), 5 * 5 * 1)

    def test_full_length(self):
        self.assertEqual(max_product([1, 3, 7, 9]), 3 * 7 * 9)
        self.assertEqual(max_product([-100, -1, 9, 5]), -100 * -1 * 9)
        self.assertEqual(max_product([100, -1, -1, 0, 5]), 100 * -1 * -1)
        self.assertEqual(max_product([-100, 1, 5, 0]), 0)
        self.assertEqual(max_product([1, 2, 3, 4, 5, -1, -2, -3, -4, -5]), -5 * -4 * 5)
        self.assertEqual(max_product([100, -1, -1, -1, -1, -1, 0, 0, 0]), 100 * -1 * -1)
        self.assertEqual(max_product([-100, -1, -1, -1, -1, -1, 0, 0, 0]), 0)
        self.assertEqual(max_product((-100, -1, -1, -1, -1, -1, 0, 0, 0)), 0)
        self.assertEqual(max_product([-1, -2, -3, -4, -5]), -1 * -2 * -3)
        self.assertEqual(max_product([0, -1, -2, -3, -4, -5]), 0)
        

class TestMaxProductFast(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(max_product_fast(None), None)
        self.assertEqual(max_product_fast([]), None)
        self.assertEqual(max_product_fast(()), None)

    def test_invalid(self):
        with self.assertRaises(TypeError):
            max_product_fast(0)

        with self.assertRaises(TypeError):
            max_product_fast({'key': 0})

    def test_short_length(self):
        self.assertEqual(max_product_fast([0]), 0)
        self.assertEqual(max_product_fast([1]), 1)
        self.assertEqual(max_product_fast((0,)), 0)
        self.assertEqual(max_product_fast((1,)), 1)
        self.assertEqual(max_product_fast([-1]), -1)
        self.assertEqual(max_product_fast([1, 0]), 1 * 0)
        self.assertEqual(max_product_fast([5, 5]), 5 * 5)
        self.assertEqual(max_product_fast([-5, 5]), -5 * 5)
        self.assertEqual(max_product_fast((1, 0)), 1 * 0)
        self.assertEqual(max_product_fast((5, 5)), 5 * 5)
        self.assertEqual(max_product_fast((-5, 5)), -5 * 5)
        self.assertEqual(max_product_fast([-5, 5, 1]), -5 * 5 * 1)
        self.assertEqual(max_product_fast([5, 5, 1]), 5 * 5 * 1)
        self.assertEqual(max_product_fast((-5, 5, 1)), -5 * 5 * 1)
        self.assertEqual(max_product_fast((5, 5, 1)), 5 * 5 * 1)

    def test_full_length(self):
        self.assertEqual(max_product_fast([1, 3, 7, 9]), 3 * 7 * 9)
        self.assertEqual(max_product_fast([-100, -1, 9, 5]), -100 * -1 * 9)
        self.assertEqual(max_product_fast([100, -1, -1, 0, 5]), 100 * -1 * -1)
        self.assertEqual(max_product_fast([-100, 1, 5, 0]), 0)
        self.assertEqual(max_product_fast([1, 2, 3, 4, 5, -1, -2, -3, -4, -5]), -5 * -4 * 5)
        self.assertEqual(max_product_fast([100, -1, -1, -1, -1, -1, 0, 0, 0]), 100 * -1 * -1)
        self.assertEqual(max_product_fast([-100, -1, -1, -1, -1, -1, 0, 0, 0]), 0)
        self.assertEqual(max_product_fast((-100, -1, -1, -1, -1, -1, 0, 0, 0)), 0)
        self.assertEqual(max_product_fast([-1, -2, -3, -4, -5]), -1 * -2 * -3)
        self.assertEqual(max_product_fast([0, -1, -2, -3, -4, -5]), 0)


if __name__ == '__main__':
    unittest.main()
