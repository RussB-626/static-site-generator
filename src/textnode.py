from enum import Enum

class TextType(Enum):
  TEXT_PLAIN = "text (plain)"
  BOLD_TEXT = "**Bold text**"
  ITALIC_TEXT = "__Italic text__"
  CODE_TEXT = "`Code text`"
  STD_LINK = "[anchor text](url)"
  IMG_LINK = "![alt text](url)"

class TextNode():
  def __init__(self, text, text_type, url):
    self.text = text
    self.text_type = text_type
    self.url = url

  def __eq__(self, other):
    if (
      self.text == other.text
      and self.text_type == other.text_type
      and self.url == other.url
    ):
      return True
    return False
  
  def __repr__(self):
    return f"TextNode({self.text}, {self.text_type}, {self.url})"