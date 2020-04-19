import pkg_resources

from unittest import TestCase, main


class TestYenerate(TestCase):
    def setUp(self):
        return

    def test_data_retrieval(self):
        exists = pkg_resources.resource_exists(__name__, "ye_album_art.jpg")
        self.assertTrue(exists)


if __name__ == "__main__":
    main()
