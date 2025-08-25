import unittest
from leafnode import LeafNode

class TestLeaveNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode(
            "a",
            "Test a tag and props",
            {"class": "greetings", "href": "https://boot.dev"}
            )
        self.assertEqual(
            node.to_html(),
            '<a class="greetings" href="https://boot.dev">Test a tag and props</a>'
            )

    def test_leaf_to_html_div(self):
        node = LeafNode(
            "div",
            "Test div tag and props",
            {"class": "greetings"}
            )
        self.assertEqual(
            node.to_html(),
            '<div class="greetings">Test div tag and props</div>'
            )

if __name__ == "__main__":
    unittest.main()