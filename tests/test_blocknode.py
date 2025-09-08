import unittest
from src.blocknode import (
    BlockType,
    block_to_block_type,
    is_heading_block,
    is_code_block,
    is_quote_block,
    is_unordered_list_block,
    is_ordered_list_block,
)

class TestBlockNode(unittest.TestCase):
    def test_is_heading_block_true(self):
        test_strings = [
            "# A valid heading",
            "### Another valid heading",
            "###### The max valid heading",            
        ]
        for text in test_strings:
            self.assertTrue(is_heading_block(text))

    def test_is_heading_block_false(self):
        test_strings = [
            "####### Too many hashtags",
            "Not a heading",
            "#Missing space"           
        ]
        for text in test_strings:
            self.assertFalse(is_heading_block(text))

    def test_blocktype_heading(self):
        test_strings = [
            "# A valid heading",
            "### Another valid heading",
            "###### The max valid heading",            
        ]
        for text in test_strings:
            block_type = block_to_block_type(text)
            self.assertEqual(
                BlockType.HEADING,
                block_type
            )

    def test_is_code_block_true(self):
        test_strings = [
            "```This is a single-line code block```",
            "```\nThis is a\nmulti-line code block\n```"
        ]
        for text in test_strings:
            self.assertTrue(is_code_block(text))

    def test_is_code_block_false(self):
        test_strings = [
            "``Not enough backticks at the start```",
            "```Not enough at the end``",
            "Text before ```the code block```",
            "```the code block``` and text after."
        ]
        for text in test_strings:
            self.assertFalse(is_code_block(text))

    def test_blocktype_code(self):
        text = "```\nThis Is a Code Block\n```"
        block_type = block_to_block_type(text)
        self.assertEqual(
            BlockType.CODE,
            block_type
        )

    def test_is_quote_block_true(self):
        test_strings = [
            "> Single Quote Line",
            "> Quote One\n> Quote Two",
            "> Quote One\n> Quote Two\n> Quote Three"
        ]
        for text in test_strings:
            self.assertTrue((is_quote_block(text)))

    def test_is_quote_block_false(self):
        test_strings = [
            " Quote One",
            "> Quote One\n Quote Two",
            "> Quote One\n Quote Two\n> Quote Three"
            "> Quote One\n>Quote Two\n> Quote Three"
        ]
        for text in test_strings:
            self.assertFalse((is_quote_block(text)))

    def test_blocktype_quote(self):
        text = "> Quote One\n> Quote Two\n> Quote Three"
        block_type = block_to_block_type(text)
        self.assertEqual(
            BlockType.QUOTE,
            block_type
        )

    def test_is_unordered_block_true(self):
        test_strings = [
            "- Value One",
            "- Value One\n- Value Two",
            "- Value One\n- Value Two\n- Value Three"
        ]
        for text in test_strings:
            self.assertTrue((is_unordered_list_block(text)))

    def test_is_unordered_block_false(self):
        test_strings = [
            " Value One",
            "- Value One\n Value Two",
            "- Value One\n Value Two\n- Value Three"
            "- Value One\n-Value Two\n- Value Three"
        ]
        for text in test_strings:
            self.assertFalse((is_unordered_list_block(text)))

    def test_blocktype_unordered_list(self):
        text = "- Value One\n- Value Two\n- Value Three"
        block_type = block_to_block_type(text)
        self.assertEqual(
            BlockType.UNORDERED_LIST,
            block_type
        )

    def test_is_ordered_block_true(self):
        test_strings = [
            "1. Value One",
            "1. Value One\n2. Value Two",
            "1. Value One\n2. Value Two\n3. Value Three"
        ]
        for text in test_strings:
            self.assertTrue((is_ordered_list_block(text)))

    def test_is_ordered_block_false(self):
        test_strings = [
            " Value One",
            "1. Value One\n Value Two",
            "1. Value One\n Value Two\n3. Value Three"
            "1. Value One\n2.Value Two\n3. Value Three"
        ]
        for text in test_strings:
            self.assertFalse((is_ordered_list_block(text)))

    def test_blocktype_ordered_list(self):
        text = "1. Value One\n2. Value Two\n3. Value Three"
        block_type = block_to_block_type(text)
        self.assertEqual(
            BlockType.ORDERED_LIST,
            block_type
        )
    
    def test_blocktype_paragraph(self):
        text = "This text contains nothing that should denote that it's anything but a paragraph block"
        block_type = block_to_block_type(text)
        self.assertEqual(
            BlockType.PARAGRAPH,
            block_type
        )


if __name__ == "__main__":
    unittest.main()
