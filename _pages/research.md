---
layout: editorial
title: "Research"
permalink: /research/
excerpt: "Articles, working papers, and applied projects."
author_profile: false
heading: "Working papers & ongoing projects"
dek: "Working papers, pre-registered projects, and earlier research-assistance work in applied microeconometrics, migration, and survey methodology."
---

<header class="page-head">
  <div class="kicker">Research</div>
  <h1 class="page-head__title">{{ page.heading | default: page.title }}</h1>
  {% if page.dek %}<p class="page-head__dek">{{ page.dek }}</p>{% endif %}
</header>

{% for section in site.data.research.sections %}
  <section class="research-section">
    <div class="section-rule">
      <h2>{{ section.title }}</h2>
      <span class="rule"></span>
    </div>

    {% if section.items and section.items.size > 0 %}
      {% for item in section.items %}
        {% assign num = forloop.index | prepend: '0' | slice: -2, 2 %}
        {% include research-entry.html item=item number=num %}
      {% endfor %}
    {% elsif section.empty_message %}
      <p class="empty-note">{{ section.empty_message }}</p>
    {% endif %}
  </section>
{% endfor %}
