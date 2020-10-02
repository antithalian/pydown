#!/usr/bin/python3

# pydown.py
# exploratory SSG for fisher.nd.edu
# see design.md for rationale

# imports
import markdown

# test header and footer
header = """<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
        
    <title>Test Website</title>
</head>

<body>"""
footer = """</body>
</html>"""

# markdown file
MD_FILE = 'markdown/test_content.md'
HTML_OUT = 'pages/index.html'

# main to whack everything together with some markdown read in
def main():
    
    with open(MD_FILE, 'r') as input_f:
        text = input_f.read()

    html = markdown.markdown(text)

    output = (header + html + footer)
    with open(HTML_OUT, 'w') as out_f:
        out_f.write(output)

if __name__ == "__main__":
    main()