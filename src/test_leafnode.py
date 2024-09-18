import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_Leaf_to_html_without_tag(self):
        node = LeafNode(value="This is a LeafNode")
        self.assertEqual(node.to_html(), "This is a LeafNode")