---
title: "Test2"
toc: true
toc_sticky: true
toc_label: "Contents"
toc_icon: "swatchbook"
permalink: /test2/
author_profile: true
header:
  overlay_color: "#000"
  overlay_filter: "0.5"
intro:
  - excerpt: "These are some of the projects that I made. Some
  are from my PhD. Some were mandatory for my courses, others just for fun or in my curious mood."
classes: wide

surgery:
  - image_path: /_data/images/unicorn.png
    image_caption: "Just a random unicorn"
    alt: "Morphological skeleton of a unicorn"
    excerpt: "The first step: get the **morphological skeleton** of a shape."
    url: "https://github.com/tanglef/project_radiosurgery_l3"
    btn_label: "Find Out More"
    btn_class: "btn--primary"
  - image_path: /_data/images/rec_surgery.png
    excerpt: "Try the algorithm on a simple shape first... more secure **especially if its related to surgery**."
  - image_path: /_data/images/surgery.png
    alt: "Radiosurgery method"
    excerpt: "We can then apply the algorithm to more complex shapes: *eg* a cerebral tumor."

shiny_app:
  - image_path: /_data/images/shiny_app.png
    alt: "main page app"
    excerpt: "Due to `shinyapps.io` time and memory limitations per-months, the app might not be always available, hence the local run option."
    url: "https://github.com/tanglef/proba_shiny_app"
    btn_label: "Find Out More"
    btn_class: "btn--primary"

chaoseverywhere:
  - image_path: https://chaoseverywhere.readthedocs.io/en/latest/_images/3d_vision.svg
    alt: "mandelbrot_3D"
    excerpt: "Use of the `Mayavi` library to make 3D visualizations."
    url: "https://github.com/tanglef/chaoseverywhere/"
    btn_label: "Find Out More"
    btn_class: "btn--primary"
  - image_path: https://chaoseverywhere.readthedocs.io/en/latest/_static/logo1_f.svg
    alt: "logo"
    excerpt: "When the bifurcation diagram and the Mandelbrot set collide... That makes **Chaoseverywhere**."
  - image_path: https://chaoseverywhere.readthedocs.io/en/latest/_images/3d_transform.svg
    excerpt: "Let the user apply any transformation on the Mandelbrot sequence."

internship:
  - image_path: /_data/images/building_interactions.png
    alt: "interaction with blocks"
    excerpt: "Memory usage with GPU was a big part of this work. Dataset dimensions quickly lead to memory errors. Interactions thus needed to be computed on the fly, but using too little memory is not efficient for GPU computation."
  - image_path: /_data/images/cd_intuition.png
    alt: "optimization"
    excerpt: "Comparison between Gradient descent and Coordinate descent. The step size choice lead to developpements of the Lanczos method in order to have quickly a good estimate of the Lipschitz constant."
  - image_path: /_data/images/transcription_dna.png
    excerpt: "Application to Genomics data."
---

{% include feature_row id="intro" type="center" %}
# High dimensional optimization for penalized linear models with interactions using graphics card computational power

Master thesis internship on the Elastic-Net estimator for the linear model with interactions using GPU acceleration.
Internship under the supervision of Benjamin Charlier and Joseph Salmon.
Based on the thesis work of Florent Bascou.
[Git Repo](https://github.com/tanglef/interactionsmodel)

[PDF report]({{ site.url }}/_data/communication/report_master.pdf)

 {% include feature_row id="internship" %}

# Chaoseverywhere package

 The main goal of this project was to create a **fully-documented Python package** that allows the user to visualization the link between the bifurcation diagram of the logistic map and the Mandelbrot set. Software Development group project. Made with Coiffier Ophélie and Gaizi Ibrahim.

<a href="https://chaoseverywhere.readthedocs.io/en/latest/index.html" class="btn btn-primary">Click here to go see the doc</a>
(don't forget to take a look at the <a href="https://chaoseverywhere.readthedocs.io/en/latest/chaos/gallery_mayavi/gallery_mayavi.html" class="btn btn-primary">galleries</a>)!

 {% include feature_row id="chaoseverywhere" %}

# Radio-surgery: bachelor degree final project
 Bachelor degree project with Clémence Roumier and Caroline Tresse on the **skeletonization** of a shape and how to **cover the most** of it with predefined-sizes rays. Methods based on *Mathématiques et technologie* by Yvan Saint-Aubin and Christiane Rousseau (Springer 2009).

{% include feature_row id="surgery" %}

# Rshiny app for interactive probabilities
 R-Shiny app to **visualize probability distributions**, make some **probability computations** easily and **interactive** dictionnary for a general bachelor-level theorems and definitions in probabilities and statistics. This was mainly to discover by my self the interactivity with the *R* programming and make it useful.

 If you prefer to run it locally, open **RStudio** or any alternative and enter in the console the following lines. You might need to install a few packages first.

```R
# install.packages(c("shiny", "plotly", "rsconnect", "shinydashboard"))
library(shiny)
runGitHub( "proba_shiny_app", "tanglef")
```

<a href="https://tanguylefort.shinyapps.io/probas/" class="btn btn-primary">Give it a try!</a>

{% include feature_row id="shiny_app" type="left" %}
