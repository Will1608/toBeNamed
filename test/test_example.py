import unittest


class TestExample(unittest.TestCase):
    def test_assert_equal(self):
        """
        2 shoudl be equal to 1+1
        """
        self.assertEqual(2, 1 + 1)
