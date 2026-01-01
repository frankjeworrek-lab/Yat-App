#!/usr/bin/env python3
import re

# Fix sidebar.py
with open('ui_nicegui/sidebar.py', 'r') as f:
    content = f.read()

# Remove all backslash escaping from f-strings
content = content.replace(r'f\"', 'f"')
content = content.replace(r'\"', '"')

with open('ui_nicegui/sidebar.py', 'w') as f:
    f.write(content)

# Fix input_area.py  
with open('ui_nicegui/input_area.py', 'r') as f:
    content = f.read()

content = content.replace(r'f\"', 'f"')
content = content.replace(r'\"', '"')

with open('ui_nicegui/input_area.py', 'w') as f:
    f.write(content)

print('Fixed syntax errors')
