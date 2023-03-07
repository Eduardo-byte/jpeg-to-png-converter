import unittest
import jpeg_to_png_converter


class TestConverter(unittest.TestCase):
    def test_input_folder_exists(self):
        result = jpeg_to_png_converter.jpeg_to_png("pokedex", "new")
        self.assertFalse(result)

    # def test_input_wrong_guess(self):
    #     result = main2.run_guess(5, 0)
    #     self.assertFalse(result)

    # def test_input_wrong_number(self):
    #     result = main2.run_guess(5, 11)
    #     self.assertFalse(result)

    # def test_input_wrong_type(self):
    #     result = main2.run_guess(5, '5')
    #     self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
