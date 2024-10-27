import unittest

from game import DecoderGame

from constants import GameConstants

class TestDecoderGame(unittest.TestCase):
    def setUp(self):
        self.game = DecoderGame()

    def test_generate_code(self):
        code = self.game.generate_code()
        self.assertEqual(len(code), GameConstants.CODE_LENGTH)
        self.assertTrue(all(d in GameConstants.DIGITS_RANGE for d in code))

    def test_validate_guess(self):
        self.assertTrue(self.game.validate_guess("1234"))
        self.assertFalse(self.game.validate_guess("123"))
        self.assertFalse(self.game.validate_guess("12a4"))
        self.assertFalse(self.game.validate_guess("1278"))

    def test_check_guess(self):
        exact, partial = self.game.check_guess("1234", "1234")
        self.assertEqual(exact, 4)
        self.assertEqual(partial, 0)

        exact, partial = self.game.check_guess("1234", "4321")
        self.assertEqual(exact, 0)
        self.assertEqual(partial, 4)

        exact, partial = self.game.check_guess("1234", "1324")
        self.assertEqual(exact, 2)
        self.assertEqual(partial, 2)

    def test_format_feedback(self):
        self.assertEqual(self.game.format_feedback(2, 1), "++-")
        self.assertEqual(self.game.format_feedback(0, 3), "---")
        self.assertEqual(self.game.format_feedback(4, 0), "++++")
        self.assertEqual(self.game.format_feedback(0, 0), "")

    def test_get_hint(self):
        code = "1234"
        used = []
        pos, val = self.game.get_hint(code, used)
        self.assertTrue(0 <= pos < GameConstants.CODE_LENGTH)
        self.assertEqual(val, code[pos])

        used = [0, 1, 2, 3]
        pos, val = self.game.get_hint(code, used)
        self.assertEqual(pos, -1)
        self.assertEqual(val, "")


if __name__ == '__main__':
    unittest.main()