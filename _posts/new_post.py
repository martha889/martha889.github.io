import os
from datetime import date
import sys

def generate_md_file(title, author="Sarthak Choudhary", category="thoughts", output_dir="."):
    # Ensure output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Get current date
    today = date.today()
    date_str = today.strftime("%Y-%m-%d")

    # Format filename and content
    title_slug = title.lower().replace(" ", "-")
    filename = f"{date_str}-{title_slug}.md"
    filepath = os.path.join(output_dir, filename)

    content = f"""---
layout: post
title: "{title}"
date: {date_str}
category: {category}
author: {author}
---
"""

    # Write to file
    with open(filepath, "w") as file:
        file.write(content)

    print(f"Markdown file created: {filepath}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <title>")
        sys.exit(1)

    title = sys.argv[1]
    generate_md_file(title)
