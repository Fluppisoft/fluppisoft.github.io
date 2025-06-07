import fire
from md2steam import markdown_to_steam_bbcode
import os
import pypandoc
import re


# Useful tool for exporting a markdown page or post to HTML or BBCode, which can be imported as a Steam announcement.
def main(md_file: str, output_path: str, format: str):
    # Load the markdown file
    with open(md_file, "r", encoding="utf-8") as file:
        content = file.read()

    # Remove front matter
    content = re.sub(r"^---\n.*?\n---\n", "", content, flags=re.DOTALL)

    # Convert image links to absolute URLs
    pattern = re.compile(r"\!\[([^\\]*?)\]\(([^\)]+?)\)")
    content = pattern.sub(
        lambda match: f"![{match.group(1)}](https://fluppisoft.com{match.group(2)})",
        content,
    )

    if format.lower() == "bb":
        # Convert markdown to BBCode
        content = markdown_to_steam_bbcode(content)
    elif format.lower() == "html":
        # Let pandoc convert to HTML
        content = pypandoc.convert_text(
            content,
            "html",
            "md",
        )
    else:
        raise NotImplementedError(
            f"Format '{format}' is not supported. Use 'bb' for BBCode or 'html' for HTML."
        )

    # Write the output file
    out_file = os.path.join(output_path, "output.txt")
    with open(out_file, "w", encoding="utf-8") as file:
        file.write(content)


if __name__ == "__main__":
    fire.Fire(main)
