import unittest


def Add(value_1, value_2):
    return value_1 + value_2


class BlackBox(unittest.TestCase):

    def add_test(self,):
        value_1 = 40
        value_2 = 30

        result = Add(value_1, value_2)
        self.assertEqual(result, 70)


if __name__ == "__main__":
    unittest.main()
