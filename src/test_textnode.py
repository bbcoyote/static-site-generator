import unittest

from textnode import TextNode



class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_text_property(self):
        node = TextNode("Hello, world!", "bold", "http://example.com")
        self.assertEqual(node.text, "Hello, world!")

    def test_text_type(self):
        node = TextNode("Hello, world!", "bold", "http://example.com")
        self.assertEqual(node.text_type, "bold")

    def test_default_url(self):
        node = TextNode("this is a text node", "bold")
        self.assertEqual(node.url, None)

    def test_url(self):
        node = TextNode("Hello, world!", "bold", "http://example.com")
        self.assertEqual(node.url, "http://example.com")

if __name__ == "__main__":
    unittest.main()