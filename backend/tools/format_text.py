import re

def format_text_tabulator(text: str):
    return re.sub(r'\t', '', text)

def format_lines_jump(text: str):
    for te in text: 
        te = re.sub(re.escape(te), '', text)
    
    return text