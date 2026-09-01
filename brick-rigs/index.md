---
layout: custom-page
title: Brick Rigs — Physics Sandbox Game on Steam
nav_title: Brick Rigs
description: Build vehicles, explore player-made creations, and unleash dynamic destruction in Brick Rigs, the overwhelmingly positively reviewed physics sandbox.
image: /assets/brick-rigs/JetAndMissille.jpg
permalink: /brick-rigs/
show_title: false
---
{::nomarkdown}
{% assign brick_rigs = site.data.brick_rigs %}
{% assign steam = brick_rigs.steam %}

<section class="game-hero brick-hero" aria-labelledby="brick-title">
  <img
    class="game-hero-art"
    src="{{ '/assets/brick-rigs/JetAndMissille.jpg' | relative_url }}"
    alt="A jet flying through an explosive Brick Rigs battle"
    width="1920"
    height="1080"
    fetchpriority="high"
  >
  <div class="game-hero-shade"></div>

  <div class="game-hero-content">
    <div class="brick-logo-frame">
      <img
        class="brick-logo"
        src="{{ '/assets/images/brick-rigs-logo.svg' | relative_url }}"
        alt="Brick Rigs"
        width="640"
        height="160"
      >
    </div>
    <h1 id="brick-title" class="sr-only">Brick Rigs physics sandbox game</h1>
    <p class="hero-copy">
      Build, drive, fly, fight, and destroy in a physics sandbox where every
      creation becomes a new way to play.
    </p>
    <div class="hero-actions">
      {% include steam-cta.html campaign="brick_rigs_page" %}
      <a class="button button-secondary" href="#gameplay">See gameplay</a>
    </div>
    {% include brick-rigs-reviews.html %}
  </div>
</section>

<section id="gameplay" class="media-feature" aria-labelledby="gameplay-title">
  <a
    class="trailer-card"
    href="{{ steam.store_url }}?utm_source={{ steam.utm_source | url_encode }}&amp;utm_medium={{ steam.utm_medium | url_encode }}&amp;utm_campaign=brick_rigs_trailer"
    target="_blank"
    rel="noopener noreferrer"
    aria-label="Watch the Brick Rigs gameplay trailer on Steam"
  >
    <img
      src="{{ '/assets/brick-rigs/Racing.png' | relative_url }}"
      alt="Brick Rigs vehicles racing on a track"
      width="1920"
      height="1080"
      loading="lazy"
    >
    <span class="play-button" aria-hidden="true">▶</span>
    <span class="trailer-label">Watch gameplay trailer on Steam</span>
  </a>
  <div class="media-feature-copy">
    <p class="eyebrow">Play your way</p>
    <h2 id="gameplay-title">No prescribed path. No wrong answers.</h2>
    <p>
      Race friends, stage rescues, command ships, build impossible machines, or
      discover what happens when they collide. Brick Rigs gives you the tools
      and lets physics write the ending.
    </p>
  </div>
</section>

<section class="content-section" aria-labelledby="features-title">
  <p class="eyebrow">The sandbox</p>
  <h2 id="features-title" class="section-title">Create it. Share it. Wreck it.</h2>
  <div class="feature-grid game-features">
    <article class="feature-card">
      <h3>Build almost anything</h3>
      <p>
        Use the powerful vehicle editor to create cars, aircraft, machines,
        buildings, and inventions nobody has named yet.
      </p>
    </article>
    <article class="feature-card">
      <h3>A universe in the Workshop</h3>
      <p>
        Jump straight into a huge collection of community-made creations, then
        adapt them or make something completely your own.
      </p>
    </article>
    <article class="feature-card">
      <h3>Dynamic destruction</h3>
      <p>
        Every crash, impact, and explosion unfolds through physics—turning
        carefully built machines into spectacular stories.
      </p>
    </article>
  </div>
</section>

<section class="screenshots-section" aria-labelledby="screenshots-title">
  <p class="eyebrow">In game</p>
  <h2 id="screenshots-title" class="section-title">Anything can happen</h2>
  <p class="section-lead">
    From precise engineering to multiplayer chaos, every session starts with a
    different idea.
  </p>
  <div class="gallery">
    {% for screenshot in brick_rigs.screenshots %}
      <a
        class="gallery-item"
        href="{{ '/assets/brick-rigs/' | append: screenshot.file | relative_url }}"
        target="_blank"
        rel="noopener noreferrer"
      >
        <img
          src="{{ '/assets/brick-rigs/' | append: screenshot.file | relative_url }}"
          alt="{{ screenshot.alt }}"
          width="1920"
          height="1080"
          loading="lazy"
        >
      </a>
    {% endfor %}
  </div>
</section>

<section class="community-panel" aria-labelledby="community-title">
  <div>
    <p class="eyebrow">Community & updates</p>
    <h2 id="community-title">A sandbox that keeps moving.</h2>
    <p>
      Brick Rigs has grown through years of development and player creativity.
      Follow development news, share what you build, or help us improve the game.
    </p>
  </div>
  <div class="support-links">
    <a href="{{ '/blog/' | relative_url }}">Read development updates</a>
    <a href="{{ brick_rigs.community.discord_url }}">Join Discord</a>
    <a href="{{ brick_rigs.community.bug_tracker_url }}">Report a bug</a>
  </div>
</section>

<section class="final-cta" aria-labelledby="final-title">
  <p class="eyebrow">Available on Steam</p>
  <h2 id="final-title">What will you build first?</h2>
  <p>Join a creative physics sandbox loved by tens of thousands of players.</p>
  {% include steam-cta.html
    campaign="brick_rigs_final_cta"
    label="Buy Brick Rigs on Steam"
  %}
  {% include brick-rigs-reviews.html compact=true %}
</section>

<nav class="legal-links" aria-label="Brick Rigs legal documents">
  <a href="{{ '/brick-rigs/eula/' | relative_url }}">EULA</a>
  <a href="{{ '/brick-rigs/privacy-policy/' | relative_url }}">Privacy policy</a>
</nav>
{:/}
