import xml.etree.ElementTree as ET

tree = ET.parse('scrap.xml')
root = tree.getroot()

# Find all occurrences of the <title> and <description> tags and print them together
title_elements = root.findall('.//title')
description_elements = root.findall('.//description')

# Open a file for writing the output
with open('output.txt', 'w', encoding='utf-8') as f:
    for title_element, description_element in zip(title_elements, description_elements):
        title = title_element.text if title_element is not None else ''
        description = description_element.text if description_element is not None else ''

        output_string = f"Title: {title}\nDescription: {description}\n=================\n"
        print(output_string)  # Print to console
        f.write(output_string)  # Write to file
