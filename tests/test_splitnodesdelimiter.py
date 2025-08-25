import unittest
from src.textnode import TextType, TextNode
from src.splitnodesdelimiter import split_nodes_delimiter, validate_delimiter



class TestSplitNodesDelimiter(unittest.TestCase):
    def test_one(self):
        text_node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([text_node], "`", TextType.CODE)
        self.assertEqual("", "")



if __name__ == "__main__":
    unittest.main()