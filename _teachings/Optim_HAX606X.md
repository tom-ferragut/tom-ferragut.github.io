---
title: HAX606X - Convex Optimization (2021-?)
falling:
  - image_path: /_teachings/data/HAX606X_optim/falling.svg
    alt: "surface"
---

This is an undergraduate course (in French!) introducing standard techniques from convex optimization. Numerical elements are provided in Python. Codes and questions are written with [Joseph Salmon](http://josephsalmon.eu).

$$f(x, y) = \frac{xy}{1+e^{x^2 - y^2}}$$
{% include feature_row id="falling" type="center" %}

## TP1: Introduction to Python

- sujet: [pdf]({{ site.url }}/_teachings/data/HAX606X_optim/tp1_sujet.pdf)
- code: [py]({{ site.url }}/_teachings/data/HAX606X_optim/tp1_sujet.py)

## TP2: First 1D algorithms: bissection and golden search methods

- sujet: [pdf]({{ site.url }}/_teachings/data/HAX606X_optim/tp2_sujet.pdf)

## TP3: Gradient descent and coordinate descent

- sujet: [pdf]({{ site.url }}/_teachings/data/HAX606X_optim/tp3_sujet.pdf)
- widgets: [fonctions]({{ site.url }}/_teachings/data/HAX606X_optim/dico_math_functions.py) [widget_level_set]({{ site.url }}/_teachings/data/HAX606X_optim/widget_level_set.py)   [widget_convergence]({{ site.url }}/_teachings/data/HAX606X_optim/widget_convergence.py)

It is necessary to have an up-to-date version of matplotlib to run the widgets. Numba and Ipython are also used.
This is the corner stone of the course !!

## TP4: Projected gradient descent and application

- sujet: [pdf]({{ site.url }}/_teachings/data/HAX606X_optim/tp4_sujet.pdf)
- widgets: [fonctions]({{ site.url }}/_teachings/data/HAX606X_optim/dico_math_functions.py) [widget_level_set]({{ site.url }}/_teachings/data/HAX606X_optim/widget_level_set.py)   [widget_convergence]({{ site.url }}/_teachings/data/HAX606X_optim/widget_convergence.py) (same as TP3, but still relevant!)
- dataset: [iowa_alcohol]({{ site.url }}/_teachings/data/HAX606X_optim/datasets/Iowa_Liquor_tp.csv)
- script with dataset: [alcohol_script]({{ site.url }}/_teachings/data/HAX606X_optim/script_season.py)

The dataset available here is an already preprocessed and subdataset of the original `Iowa_Liquor` dataset (link in the `alcohol_script` file).
