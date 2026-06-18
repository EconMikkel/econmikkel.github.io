---
layout: editorial
permalink: /
title: ""
excerpt: "Research, working papers, and short notes."
author_profile: false
redirect_from:
  - /about/
  - /about.html
---

<section class="home-lead-block">
  <p class="home-standfirst">{{ site.author.bio }}</p>
  <p class="home-lead-2">This site brings together my current research, academic writing, and shorter notes on methods, data, and policy questions.</p>
  <div class="home-actions">
    <a class="btn btn--solid" href="{{ '/research/' | relative_url }}">View Research</a>
    <a class="btn btn--ghost" href="{{ '/notes/' | relative_url }}">Browse Notes</a>
  </div>
</section>

<div class="home-grid">
  <!-- Main: The Latest -->
  <div class="home-main">
    <div class="section-rule">
      <h2>The Latest</h2>
      <span class="rule"></span>
    </div>
    {% include news-list.html limit=4 %}
  </div>

  <!-- Rail -->
  <aside class="rail">
    <figure class="rail__figure">
      <img src="{{ '/images/profile.jpg' | relative_url }}" alt="{{ site.author.name }}">
      <figcaption class="rail__caption">{{ site.author.name }}, {{ site.author.location }}.</figcaption>
    </figure>

    <div class="rail__block rail__block--first">
      <div class="rail__label">Affiliations</div>
      <div class="rail__value">
        {% for emp in site.author.employer %}{{ emp }}{% unless forloop.last %}<br>{% endunless %}{% endfor %}
      </div>
    </div>

    <div class="rail__block">
      <div class="rail__label">Location</div>
      <div class="rail__value">{{ site.author.location }}</div>
    </div>

    <div class="rail__block">
      <div class="rail__label">Email</div>
      <div class="rail__value"><a href="mailto:{{ site.author.email }}">{{ site.author.email }}</a></div>
    </div>

    <div class="rail__block">
      <div class="rail__label">Profiles</div>
      <div class="rail__profiles">
        {% if site.author.googlescholar %}<a href="{{ site.author.googlescholar }}" target="_blank" rel="noopener">Google Scholar →</a>{% endif %}
        {% if site.author.orcid %}<a href="{{ site.author.orcid }}" target="_blank" rel="noopener">ORCID →</a>{% endif %}
      </div>
    </div>
  </aside>
</div>
