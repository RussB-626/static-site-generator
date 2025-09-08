from enum import Enum
import re


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    if is_heading_block(block):
        return BlockType.HEADING
    if is_code_block(block):
        return BlockType.CODE
    if is_quote_block(block):
        return BlockType.QUOTE
    if is_unordered_list_block(block):
        return BlockType.UNORDERED_LIST
    if is_ordered_list_block(block):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

def is_heading_block(text):
    if len(text) == 0:
        return False
    pattern = r"^#{1,6} "
    return re.match(pattern, text)

def is_code_block(text):
    if len(text) == 0:
        return False
    if text[:3] != "```":
        return False
    if text[-3:] != "```":
        return False
    return True

def is_quote_block(text):
    if len(text) == 0:
        return False
    lines = text.split('\n')
    for line in lines:
        if line[:2] != "> ":
            return False
    return True

def is_unordered_list_block(text):
    if len(text) == 0:
        return False
    lines = text.split('\n')
    for line in lines:
        if line[:2] != "- ":
            return False
    return True

def is_ordered_list_block(text):
    pattern = r"^\d\. "
    count = 1
    if len(text) == 0:
        return False
    lines = text.split('\n')
    for line in lines:
        if not re.match(pattern, line):
            return False
        if line[:1] != str(count):
            return False
        else:
            count += 1
    return True