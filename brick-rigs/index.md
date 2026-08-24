---
layout: custom-page
title: Brick Rigs
banner: "/assets/images/brick-rigs-logo.svg"
---

Do whatever you want in a physics sandbox full of chaotic destruction, endless player-made creations and unpredictable adventures. Build, destroy, roleplay and mess around solo or with friends!

{::nomarkdown}
<section class="screenshots-section">
  <h2 class="screenshots-title">Screenshots</h2>
  <p class="screenshots-subtitle">A quick look at the worlds and creations you can build in Brick Rigs.</p>
  <div class="gallery">
  {%- for image in site.static_files -%}
    {%- if image.path contains 'assets/brick-rigs/' -%}
      <a class="gallery-item" href="{{ image.path | relative_url }}" target="_blank" rel="noopener noreferrer">
        <img src="{{ image.path | relative_url }}" alt="Brick Rigs screenshot {{ forloop.index }}">
      </a>
    {%- endif -%}
  {%- endfor -%}
  </div>
</section>

<section class="content-section">
  <h2 class="section-title">Join the community</h2>
<div class="widget-container">
{% include widget.html
  image="/assets/images/steam-logo.png"
  text="Buy Brick Rigs on Steam."
  ref="https://steam.brick-rigs.com/"
%}

{% include widget.html
image="/assets/images/discord-logo.png"
text="Join the official Brick Rigs Discord server."
ref="https://discord.brick-rigs.com/"
%}

{% include widget.html
image="/assets/images/bugs-logo.png"
text="Report bugs on the official bug tracker."
ref="https://bugs.brick-rigs.com/"
%}
</div>
</section>

<section class="content-section">
  <h2 class="section-title">Legal</h2>
  <p class="section-lead">The terms you agree to when playing Brick Rigs, and how we handle your data.</p>
  <div class="quick-links">
    <a href="{{ '/brick-rigs/eula/' | relative_url }}">End User License Agreement</a>
    <a href="{{ '/brick-rigs/privacy-policy/' | relative_url }}">Privacy Policy</a>
  </div>
</section>
{:/}