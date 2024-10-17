import unittest
from PIL import Image


class TestBackground(unittest.TestCase):
    def setUp(self):
        self.image = Image.open("tests/fixtures/background.png")
        self.pxs = self.image.load()
        return super().setUp()

    def test_simple_positive(self):
        self.assertIsNotNone(self.image)
        self.assertIsNotNone(self.pxs)

    def test_white_pxls(self):
        px0 = self.pxs[0, 0]
        self.assertEqual(px0, (255, 255, 255))

    def test_black_pxls(self):
        px1 = self.pxs[1, 0]
        self.assertEqual(px1, (0, 0, 0))

    def test_almost_black_pxls(self):
        px2 = self.pxs[2, 0]
        self.assertEqual(px2, (1, 2, 3))
