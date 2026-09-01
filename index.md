---
layout: custom-page
title: Fluppisoft — Independent Developer of Brick Rigs
nav_title: Home
description: Fluppisoft is the independent German developer and publisher of Brick Rigs, the overwhelmingly positively reviewed physics sandbox on Steam.
image: /assets/brick-rigs/Pursuit.jpg
permalink: /
show_title: false
---
{::nomarkdown}
<section class="game-hero home-hero" aria-labelledby="home-title">
  <img
    class="game-hero-art"
    src="{{ '/assets/brick-rigs/Pursuit.jpg' | relative_url }}"
    alt="A police pursuit through Bricksville in Brick Rigs"
    width="1920"
    height="1080"
    fetchpriority="high"
  >
  <div class="game-hero-shade"></div>

  <div class="game-hero-content">
    <p class="eyebrow">Independent game development from Germany</p>
    <h1 id="home-title">We make <span>Brick Rigs.</span></h1>
    <p class="hero-copy">
      Build anything. Drive everything. Destroy it spectacularly. Brick Rigs is
      a physics sandbox shaped by creativity, chaos, and its community.
    </p>
    <div class="hero-actions">
      {% include steam-cta.html campaign="homepage" %}
      <a class="button button-secondary" href="{{ '/brick-rigs/' | relative_url }}">
        Explore Brick Rigs
      </a>
    </div>
    {% include brick-rigs-reviews.html %}
  </div>
</section>

<section class="content-section intro-section" aria-labelledby="studio-title">
  <p class="eyebrow">Fluppisoft</p>
  <h2 id="studio-title" class="section-title">Games made independently.</h2>
  <p class="section-lead">
    Fluppisoft is an independent game studio based in Bavaria, Germany. We
    develop and publish our own games, including Brick Rigs. We care about
    giving ideas the time they need, supporting our games after release, and
    listening to the people who play them.
  </p>

  <div class="feature-grid studio-values">
    <article class="feature-card">
      <span class="feature-number">01</span>
      <h3>Creative independence</h3>
      <p>
        We make our own development decisions and follow ideas that we think can
        lead to interesting games.
      </p>
    </article>
    <article class="feature-card">
      <span class="feature-number">02</span>
      <h3>Long-term support</h3>
      <p>
        Releasing a game is not the end of the work. We continue fixing
        problems, improving systems, and adding worthwhile features.
      </p>
    </article>
    <article class="feature-card">
      <span class="feature-number">03</span>
      <h3>Growing with the community</h3>
      <p>
        Player feedback helps us understand what works, what needs attention,
        and where our games can improve over time.
      </p>
    </article>
  </div>
</section>

<section class="featured-game" aria-labelledby="featured-title">
  <div class="featured-game-media">
    <img
      src="{{ '/assets/brick-rigs/Editor.jpg' | relative_url }}"
      alt="Building a detailed vehicle in the Brick Rigs editor"
      width="1920"
      height="1080"
      loading="lazy"
    >
  </div>
  <div class="featured-game-copy">
    <p class="eyebrow">Our game</p>
    <h2 id="featured-title">Your imagination, with physics.</h2>
    <p>
      Build detailed machines, download creations from the Steam Workshop, race
      through open environments, or turn the whole thing into a glorious pile
      of bricks—alone or online.
    </p>
    <a class="text-link" href="{{ '/brick-rigs/' | relative_url }}">
      Discover Brick Rigs <span aria-hidden="true">→</span>
    </a>
  </div>
</section>
{:/}
