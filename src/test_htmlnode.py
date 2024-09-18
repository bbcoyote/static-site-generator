import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(props={"href": "https://www.example.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.example.com" target="_blank"')

    def test_repr(self):
        node = HTMLNode("p", "Hello, world!")
        print(f"print! {repr(node)}")
        self.assertEqual(repr(node), "HTMLNode(tag='p', value='Hello, world!', children=None, props=None)")

    def test_to_html_raises_error(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()

if __name__ == "__main__":
    unittest.main()