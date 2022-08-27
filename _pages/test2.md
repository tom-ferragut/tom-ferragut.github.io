---
title: "test2"
permalink: /test2/
author_profile: true
header:
  overlay_color: "#000"
  overlay_filter: "0.5"
intro:
  - excerpt: "Some figures from various projects I worked on. "
classes: wide


internship:
  - image_path: /_data/images/building_interactions.png
    alt: "interaction with blocks"
    excerpt: "Memory usage with GPU was a big part of this work. Dataset dimensions quickly lead to memory errors. Interactions thus needed to be computed on the fly, but using too little memory is not efficient for GPU computation."
  - image_path: /_data/images/cd_intuition.png
    alt: "optimization"
    excerpt: "Comparison between Gradient descent and Coordinate descent. The step size choice lead to developpements of the Lanczos method in order to have quickly a good estimate of the Lipschitz constant."
  - image_path: /_data/images/transcription_dna.png
    excerpt: "Application to Genomics data."
    
master:
  -blabla

---

{% include feature_row id="intro" type="center" %}
# Hurwitz Problem

Master thesis internship on the Elastic-Net estimator for the linear model with interactions using GPU acceleration.
Internship under the supervision of Benjamin Charlier and Joseph Salmon.
Based on the thesis work of Florent Bascou.
[Git Repo](https://github.com/tanglef/interactionsmodel)

[PDF report]({{ site.url }}/_data/communication/report_master.pdf)

 {% include feature_row id="internship" %}

# 2nd Theme

 Blabla
