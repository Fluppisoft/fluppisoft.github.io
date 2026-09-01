import re
from pathlib import Path

import fire
from md2steam import markdown_to_steam_bbcode
import pypandoc


SITE_URL = "https://fluppisoft.com"
IMAGE_PATTERN = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")


def make_image_url_absolute(match: re.Match[str]) -> str:
    """Convert root-relative Markdown image URLs to production URLs."""
    alt_text, image_url = match.groups()
    if image_url.startswith("/"):
        image_url = f"{SITE_URL}{image_url}"
    return f"![{alt_text}]({image_url})"


def main(md_file: str, output_path: str, format: str):
    """Export a Jekyll Markdown file as HTML or Steam-compatible BBCode."""
    content = Path(md_file).read_text(encoding="utf-8")

    # Remove front matter
    content = re.sub(r"^---\n.*?\n---\n", "", content, flags=re.DOTALL)

    # Convert image links to absolute URLs
    content = IMAGE_PATTERN.sub(make_image_url_absolute, content)

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
    output_directory = Path(output_path)
    output_directory.mkdir(parents=True, exist_ok=True)
    (output_directory / "output.txt").write_text(content, encoding="utf-8")


if __name__ == "__main__":
    fire.Fire(main)
