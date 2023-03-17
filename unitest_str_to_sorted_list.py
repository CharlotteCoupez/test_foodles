import unittest
from str_to_sorted_list import str_to_sorted_list

class Test_str_to_sorted_list(unittest.TestCase):

    def test_multiple_word(self):
        n = 3
        sentence = "baz bar foo foo zblah zblah zblah baz toto bar"
        result =  [("zblah", 3), ("bar", 2), ("baz", 2)]
        self.assertEqual(str_to_sorted_list(sentence, n), result)

    def test_sentence_null(self):
        n = 3
        sentence = ""
        result = None
        self.assertEqual(str_to_sorted_list(sentence, n), result)

    def test_n_neg(self):
        n = -1
        sentence = "baz bar foo foo zblah zblah zblah baz toto bar"
        result = None
        self.assertEqual(str_to_sorted_list(sentence, n), result)


if __name__ == '__main__':
    unittest.main()
