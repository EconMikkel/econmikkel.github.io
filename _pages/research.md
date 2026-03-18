---
layout: archive
title: "Research"
permalink: /research/
excerpt: "Articles, working papers, and applied projects."
author_profile: false
---

<div class="page-intro">
  <p>This page is driven by a single data file: <code>_data/research.yml</code>. Add a new paper to the relevant section, include co-authors and links, and it will appear here automatically.</p>
</div>

{% for section in site.data.research.sections %}
  <section class="research-section">
    <div class="research-section__header">
      <h2>{{ section.title }}</h2>
      {% if section.description %}
        <p>{{ section.description }}</p>
      {% endif %}
    </div>

    {% if section.items and section.items.size > 0 %}
      <div class="research-list">
        {% for item in section.items %}
          {% include research-entry.html item=item %}
        {% endfor %}
      </div>
    {% elsif section.empty_message %}
      <p class="empty-state">{{ section.empty_message }}</p>
    {% endif %}
  </section>
{% endfor %}
