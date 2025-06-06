import fire
import os
import pypandoc
import re


# Useful tool for exporting a markdown page or post to HTML, which can be imported as a Steam announcement.
def main(md_file: str, output_path: str):
    # Load the markdown file
    with open(md_file, "r", encoding="utf-8") as file:
        content = file.read()

    # Convert image links to absolute URLs
    pattern = re.compile(r"\!\[([^\\]*?)\]\(([^\)]+?)\)")
    content = pattern.sub(
        lambda match: f"![{match.group(1)}](https://fluppisoft.com{match.group(2)})",
        content,
    )

    # Let pandoc handle the conversion
    output = pypandoc.convert_text(
        content,
        "html",
        "md",
    )

    # Write the output to an HTML file
    filename = os.path.splitext(os.path.basename(md_file))[0]
    html_file = os.path.join(output_path, filename + ".html")
    with open(html_file, "w", encoding="utf-8") as file:
        file.write(output)


if __name__ == "__main__":
    fire.Fire(main)
