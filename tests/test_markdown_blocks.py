import unittest
from src.markdown_blocks import (
    BlockType,
    markdown_to_blocks,
    block_to_block_type,
    markdown_to_html_node
)


class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        block = "- list\n- items"
        self.assertEqual(block_to_block_type(block), BlockType.ULIST)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), BlockType.OLIST)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_heading(self):
        md = """
# **This is a Header**

paragraph text in a p
tag here

This is another paragraph with _italic_ text and `code` here
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1><b>This is a Header</b></h1><p>paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )
        

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_quoteblock(self):
        md = """
> This is a **quote** block
> with _multiple_ lines of
> quote text
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a <b>quote</b> block\nwith <i>multiple</i> lines of\nquote text</blockquote></div>",
        )

    def test_olistblock(self):
        md = """
1. This is an **ordered list** block
2. with _multiple_ lines of
3. items in the list
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>This is an <b>ordered list</b> block</li><li>with <i>multiple</i> lines of</li><li>items in the list</li></ol></div>",
        )

    def test_ulistblock(self):
        md = """
- This is an **unordered list** block
- with _multiple_ lines of
- items in the list
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is an <b>unordered list</b> block</li><li>with <i>multiple</i> lines of</li><li>items in the list</li></ul></div>",
        )

if __name__ == "__main__":
    unittest.main()