---
layout: splash
permalink: /
title: ""
excerpt: "Research, working papers, and short notes."
author_profile: false
redirect_from:
  - /about/
  - /about.html
---

<section class="home-hero">
  <div class="home-hero__content">
    <h1 class="home-hero__title">{{ site.author.name }}</h1>
    <p class="home-lead">{{ site.author.bio }}</p>
    <p class="home-lead">This site brings together my current research, academic writing, and shorter notes on methods, data, and policy questions.</p>

    <div class="home-actions">
      <a class="home-button home-button--primary" href="{{ '/research/' | relative_url }}">View research</a>
      <a class="home-button home-button--ghost" href="{{ '/notes/' | relative_url }}">Browse notes</a>
    </div>
  </div>

  <aside class="home-hero__profile">
    <img src="{{ '/images/profile.jpg' | relative_url }}" alt="{{ site.author.name }}">

    <div class="home-profile__list">
      <div class="home-profile__row">
        <span class="home-profile__label">Affiliation</span>
        <span class="home-profile__value">{{ site.author.employer }}</span>
      </div>
      <div class="home-profile__row">
        <span class="home-profile__label">Location</span>
        <span class="home-profile__value">{{ site.author.location }}</span>
      </div>
      <div class="home-profile__row">
        <span class="home-profile__label">Email</span>
        <span class="home-profile__value"><a href="mailto:{{ site.author.email }}">{{ site.author.email }}</a></span>
      </div>
      <div class="home-profile__row">
        <span class="home-profile__label">Profiles</span>
        <span class="home-profile__value"><a href="{{ site.author.googlescholar }}">Google Scholar</a> | <a href="{{ site.author.orcid }}">ORCID</a></span>
      </div>
    </div>
  </aside>
</section>

<section class="home-section">
  <div class="section-heading">
    <div>
      <h2>New news</h2>
    </div>
  </div>

  <div class="home-grid home-grid--news">
    {% include news-list.html limit=4 %}
  </div>
</section>

<section class="home-section">
  <div class="section-heading">
    <div>
      <h2>Recent notes</h2>
      <p>Smaller analyses, open questions, and blog-style writing.</p>
    </div>
    <a href="{{ '/notes/' | relative_url }}">See all notes</a>
  </div>

  <div class="home-grid home-grid--notes">
    {% include notes-list.html limit=3 %}
  </div>
</section>
