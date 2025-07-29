---
layout: custom-page
title: Brick Rigs
banner: "/assets/images/brick-rigs-logo.png"
permalink: /brick-rigs/
---

Brick Rigs is a physics sandbox game running on Unreal Engine 4. It focuses on freedom, creativity, community and destruction.

{::nomarkdown}
<div class="gallery">
  {%- for image in site.static_files -%}
    {%- if image.path contains 'assets/brick-rigs/' -%}
      <div class="gallery-item">
        <img src="{{ image.path | relative_url }}" alt="{{ image.name }}">
      </div>
    {%- endif -%}
  {%- endfor -%}
</div>

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
{:/}