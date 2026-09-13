#!/usr/bin/env python3

import unittest

from src.anagrams import anagrams


class TestAnagrams(unittest.TestCase):

    def test_returns_a_bool(self):
        result = anagrams("a", "a")
        self.assertIsInstance(
            result, bool,
            msg="anagrams('a', 'a') should return a bool, not %r."
                % (type(result),))

    def test_anagram_pairs(self):
        test_cases = [
            ("house", "esuoh"),
            ("tar", "rat"),
            ("stressed", "desserts"),
            ("cat", "act"),
            ("save", "vase"),
            ("salvages", "lasvegas"),
            ("state", "taste"),
            ("python", "nythop"),
        ]
        for word1, word2 in test_cases:
            with self.subTest(word1=word1, word2=word2):
                result = anagrams(word1, word2)
                self.assertTrue(
                    result,
                    msg="anagrams(%r, %r) should be True: the two words "
                        "use exactly the same letters."
                        % (word1, word2))

    def test_non_anagram_pairs(self):
        test_cases = [
            ("house", "mouse"),
            ("tree", "three"),
            ("desserts", "reindeers"),
            ("test", "set"),
            ("python", "java"),
        ]
        for word1, word2 in test_cases:
            with self.subTest(word1=word1, word2=word2):
                result = anagrams(word1, word2)
                self.assertFalse(
                    result,
                    msg="anagrams(%r, %r) should be False: the two words "
                        "do not use exactly the same letters."
                        % (word1, word2))

    def test_identical_words_are_anagrams(self):
        result = anagrams("cat", "cat")
        self.assertTrue(
            result,
            msg="anagrams('cat', 'cat') should be True: a word is always "
                "an anagram of itself.")

    def test_empty_strings_are_anagrams(self):
        result = anagrams("", "")
        self.assertTrue(
            result,
            msg="anagrams('', '') should be True: two empty strings use "
                "the same (empty) set of letters.")


if __name__ == '__main__':
    unittest.main()
