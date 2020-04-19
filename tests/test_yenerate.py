import pkg_resources
import tempfile
import shutil

from yenerate import yenerate
from unittest import TestCase, main


class TestYenerate(TestCase):
    def setUp(self):
        self.root = tempfile.mkdtemp(prefix="yenerate_test")

    def tearDown(self):
        shutil.rmtree(self.root)

    def test_yenerate(self):
        output = yenerate.create_image("sample")
        self.assertIsNotNone(output)

    def test_wrap_line(self):
        text = "this is a short text"

        wrapped, _ = yenerate.wrap_text(text, max_width=100)
        self.assertEqual(wrapped, text)

        wrapped, _ = yenerate.wrap_text(text, max_width=10)
        self.assertEqual(wrapped, "this is a\nshort text")


if __name__ == "__main__":
    main()
