import re
from enum import Enum
from src.htmlnode import (
    HTMLNode,
    LeafNode,
    ParentNode
)
from src.textnode import (
    TextType,
    TextNode,
    text_node_to_html_node,
)
from src.inline_markdown import text_to_textnodes

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    OLIST = "ordered_list"
    ULIST = "unordered_list"

def markdown_to_blocks(markdown):
    blocks = markdown.split('\n\n')
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks

def block_to_block_type(block):
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.ULIST
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.OLIST
    return BlockType.PARAGRAPH

def markdown_to_html_node(md):
    blocks = markdown_to_blocks(md)
    parent_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        parent_node = block_to_parentnode(block, block_type)
        parent_nodes.append(parent_node)
    return ParentNode("div",parent_nodes)

def block_to_parentnode(block, block_type):
    if block_type == BlockType.PARAGRAPH:
        return paragraph_block_to_parentnode(block)
    elif block_type == BlockType.HEADING:
        return heading_block_to_parentnode(block)
    elif block_type == BlockType.CODE:
        return code_block_to_parentnode(block)
    elif block_type == BlockType.QUOTE:
        return quote_block_to_parentnode(block)
    elif block_type == BlockType.OLIST:
        return olist_block_to_parentnode(block)
    elif block_type == BlockType.ULIST:
        return ulist_block_to_parentnode(block)

def paragraph_block_to_parentnode(block):
    text = block.replace("\n", " ")
    children = text_to_children(text)
    return ParentNode("p", children)

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = []
    for text_node in text_nodes:
        html_nodes.append(text_node_to_html_node(text_node))
    return html_nodes

def heading_block_to_parentnode(block):
    space = block.find(" ")
    text = None
    hash_count = None
    if space > 0:
        text = block[space+1:]
        hash_count = len(block[:space])
    else:
        text = block
        hash_count = 1
    text = text.replace("\n", " ")    
    children = text_to_children(text)
    return ParentNode(f"h{hash_count}", children)

def code_block_to_parentnode(block):
    text = block[4:][:-3]
    text_node = TextNode(text,TextType.CODE)
    html_node = text_node_to_html_node(text_node)
    return ParentNode("pre",[html_node])

def quote_block_to_parentnode(block):
    lines = block.split("\n")
    text_lines = []
    for line in lines:
        text_lines.append(line[2:])
    text = "\n".join(text_lines)
    children = text_to_children(text)
    return ParentNode("blockquote",children)

def olist_block_to_parentnode(block):
    lines = block.split("\n")
    parent_nodes = []
    i = 1
    for line in lines:
        to_find = f"{i}. "
        text = line[len(to_find):]
        children = text_to_children(text)
        parent_nodes.append(ParentNode("li",children))
        i += 1
    return ParentNode("ol",parent_nodes)

def ulist_block_to_parentnode(block):
    lines = block.split("\n")
    parent_nodes = []
    for line in lines:
        text = line[2:]
        children = text_to_children(text)
        parent_nodes.append(ParentNode("li",children))
    return ParentNode("ul",parent_nodes)