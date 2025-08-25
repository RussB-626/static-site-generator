from .textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    nodes = []    
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            nodes.append(old_node)
        elif validate_delimiter(old_node.text, delimiter):
            split_lines = old_node.text.split(delimiter)
            for i, text in enumerate(split_lines):
                    if i % 2 == 0:
                         nodes.append(TextNode(text, TextType.TEXT))
                    else:
                         nodes.append(TextNode(text, TextType.CODE))
    return nodes

def validate_delimiter(value, delimiter):
    count = value.count(delimiter)
    if count % 2 != 0:
        raise ValueError(f'unmatched delimiter: "{delimiter}" found in string')
    return True