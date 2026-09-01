# Fluppisoft website

The Fluppisoft website is a static Jekyll site based on the Minima theme. It is
published at [fluppisoft.com](https://fluppisoft.com/).

## Local development

Install the Ruby dependencies and start the development server:

```sh
bundle install
bundle exec jekyll serve
```

Run a production-style build before committing changes:

```sh
bundle exec jekyll build
```

## Content structure

- `index.md` contains the homepage.
- `brick-rigs/index.md` contains the Brick Rigs landing page.
- `_posts/` contains development news.
- `_data/brick_rigs.yml` is the single source for Steam details, review scores,
  community links, and the screenshot list.
- `_includes/` contains shared Liquid components.
- `_sass/minima/custom-styles.scss` contains site-specific styling on top of
  Minima.

Update Steam review values only in `_data/brick_rigs.yml`. Use the shared
`steam-cta.html` include for new purchase links so tracking parameters stay
consistent.

The helper in `python/export_markdown.py` converts a post to HTML or
Steam-compatible BBCode. Its Python dependencies are listed in
`python/requirements.txt`.
