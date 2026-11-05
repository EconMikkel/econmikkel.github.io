---
layout: editorial
title: "Presentations"
permalink: /presentations/
excerpt: "Talks, workshops, and seminar presentations."
author_profile: false
heading: "Presentations"
dek: "Talks, workshops, and seminar presentations."
---

<header class="page-head">
  <div class="kicker">Presentations</div>
  <h1 class="page-head__title">{{ page.heading | default: page.title }}</h1>
  {% if page.dek %}<p class="page-head__dek">{{ page.dek }}</p>{% endif %}
</header>

{% assign talks = site.data.presentations.presentations %}
{% if talks and talks.size > 0 %}
  {% assign years = talks | group_by: "year" | sort: "name" | reverse %}
  {% for group in years %}
    <section class="talks-section">
      <div class="section-rule">
        <h2>{{ group.name }}</h2>
        <span class="rule"></span>
      </div>
      <ul class="talks">
        {% for talk in group.items %}
          <li class="talk">
            <div class="talk__title">
              {%- if talk.url -%}<a href="{{ talk.url }}" target="_blank" rel="noopener">{{ talk.title }}</a>{%- else -%}{{ talk.title }}{%- endif -%}
            </div>
            <div class="talk__meta">
              {%- if talk.place %}<span class="talk__place">{{ talk.place }}</span>{% endif -%}
              {%- if talk.context %}{% if talk.place %} &nbsp;·&nbsp; {% endif %}{{ talk.context }}{% endif -%}
              {%- if talk.date %} &nbsp;·&nbsp; {{ talk.date }}{% endif -%}
            </div>
          </li>
        {% endfor %}
      </ul>
    </section>
  {% endfor %}
{% else %}
  <p class="empty-note">No presentations added yet.</p>
{% endif %}
