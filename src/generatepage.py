import os
from src.markdown_blocks import markdown_to_html_node
from src.inline_markdown import extract_title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    md_file = get_file_contents(from_path)
    template_file = get_file_contents(template_path)
    html_node = markdown_to_html_node(md_file)
    title = extract_title(md_file)    
    template_file = template_file.replace("{{ Title }}", title)
    template_file = template_file.replace("{{ Content }}", html_node.to_html())
    write_file_contents(template_file, dest_path)
    

def get_file_contents(target_path):
    target_abs = os.path.abspath(target_path)
    if not os.path.isfile(target_abs):
        raise Exception(f'{target_path} is not a valid file.')
    
    try:
        with open(target_abs, "r") as reader:
            file_contents = reader.read(-1)
            return file_contents
    except Exception as e:
        raise Exception(f'Error reading file "{target_path}": {e}')
    
def write_file_contents(contents, target_path):
    target_abs = os.path.abspath(target_path)
    try:
        with open(target_abs, "w") as writer:
            writer.write(contents)
        return f'Successfully wrote to "{target_path}" ({len(contents)} characters written).'
    except Exception as e:
        raise Exception(f'Error writing to file "{target_path}": {e}')