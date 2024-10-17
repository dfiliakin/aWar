import unittest
import os
from pathlib import Path


class TestPalette(unittest.TestCase):
    def setUp(self):
        self.palette_folder_path = Path("assets/sprites/background_tiles")
        return super().setUp()
