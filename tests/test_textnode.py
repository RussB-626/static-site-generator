import unittest
from src.textnode import (
    TextNode,
    TextType,
    text_node_to_html_node,
    # text_to_textnodes
)


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node2", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )


class TestTextnodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        text_to_match = "This is a text node"
        tag_to_match = None
        node = TextNode(text_to_match, TextType.TEXT)
        html_node = text_node_to_html_node(node)
        # --- TESTS
        self.assertEqual(html_node.tag, tag_to_match)
        self.assertEqual(html_node.value, text_to_match)
        self.assertEqual(html_node.to_html(), text_to_match)
        self.assertEqual(repr(html_node), f"LeafNode({tag_to_match}, {text_to_match}, None)")

    def test_bold(self):
        text_to_match = "This is a bold text node"
        tag_to_match = "b"
        node = TextNode(text_to_match, TextType.BOLD)
        html_node = text_node_to_html_node(node)
        # --- TESTS
        self.assertEqual(html_node.tag, tag_to_match)
        self.assertEqual(html_node.value, text_to_match)
        self.assertEqual(html_node.to_html(), f"<{tag_to_match}>{text_to_match}</{tag_to_match}>")
        self.assertEqual(repr(html_node), f"LeafNode({tag_to_match}, {text_to_match}, None)")

    def test_italic(self):
        text_to_match = "This is an italic text node"
        tag_to_match = "i"
        node = TextNode(text_to_match, TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        # --- TESTS
        self.assertEqual(html_node.tag, tag_to_match)
        self.assertEqual(html_node.value, text_to_match)
        self.assertEqual(html_node.to_html(), f"<{tag_to_match}>{text_to_match}</{tag_to_match}>")
        self.assertEqual(repr(html_node), f"LeafNode({tag_to_match}, {text_to_match}, None)")

    def test_code(self):
        text_to_match = "This is a code text node"
        tag_to_match = "code"
        node = TextNode(text_to_match, TextType.CODE)
        html_node = text_node_to_html_node(node)
        # --- TESTS
        self.assertEqual(html_node.tag, tag_to_match)
        self.assertEqual(html_node.value, text_to_match)
        self.assertEqual(
            html_node.to_html(),
            f"<{tag_to_match}>{text_to_match}</{tag_to_match}>"
        )
        self.assertEqual(
            repr(html_node),
            f"LeafNode({tag_to_match}, {text_to_match}, None)"
        )

    def test_link(self):
        text_to_match = "This is a link node"
        tag_to_match = "a"
        url_to_match = "https://link.com"
        node = TextNode(text_to_match, TextType.LINK, url_to_match)
        html_node = text_node_to_html_node(node)
        # --- TESTS
        self.assertEqual(html_node.tag, tag_to_match)
        self.assertEqual(html_node.value, text_to_match)
        self.assertEqual(
            html_node.to_html(), 
            f'<{tag_to_match} href="{url_to_match}">{text_to_match}</{tag_to_match}>'
        )
        repr_val = repr(html_node)
        self.assertEqual(
            repr(html_node),
            f"LeafNode({tag_to_match}, {text_to_match}, {{'href': '{url_to_match}'}})"
        )

    def test_image(self):
        text_to_match = "This is an image node"
        tag_to_match = "img"
        url_to_match = "https://img.com"
        node = TextNode(text_to_match, TextType.IMAGE, url_to_match)
        html_node = text_node_to_html_node(node)
        # --- TESTS
        self.assertEqual(html_node.tag, tag_to_match)
        self.assertEqual(html_node.value, "")
        html = html_node.to_html()
        self.assertEqual(
            html_node.to_html(), 
            f'<{tag_to_match} src="{url_to_match}" alt="{text_to_match}"></{tag_to_match}>'
        )
        self.assertEqual(
            repr(html_node),
            f"LeafNode({tag_to_match}, , {{'src': '{url_to_match}', 'alt': '{text_to_match}'}})"
        )


if __name__ == "__main__":
    unittest.main()