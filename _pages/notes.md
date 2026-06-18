---
layout: editorial
title: "Notes"
permalink: /notes/
excerpt: "Short essays, smaller analyses, and research questions."
author_profile: false
heading: "Notes"
dek: "Blog-style posts: smaller analyses, open questions, and musings on methods and data. Not peer-reviewed and by no means formal research."
---

<header class="page-head">
  <div class="kicker">Notes</div>
  <h1 class="page-head__title">{{ page.heading | default: page.title }}</h1>
  {% if page.dek %}<p class="page-head__dek">{{ page.dek }}</p>{% endif %}
</header>

{% include notes-list.html %}
