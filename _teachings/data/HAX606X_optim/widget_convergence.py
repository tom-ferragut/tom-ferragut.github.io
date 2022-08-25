import numpy as np

# pip install numba if needed
from numba import njit  # noga

from IPython import get_ipython, display  # noqa


# pip install ipympl if needed
get_ipython().run_line_magic("matplotlib", "widget")

import matplotlib.pyplot as plt
import matplotlib

cmap_reversed = matplotlib.cm.get_cmap("Blues_r")
from mpl_toolkits import mplot3d
from mpl_toolkits.axes_grid1 import make_axes_locatable
from ipywidgets import (
    interactive,
    fixed,
    FloatRangeSlider,
    FloatSlider,
    IntSlider,
    SelectMultiple,
    Layout,
)

import ipywidgets as widgets

from dico_math_functions import (
    quad,
    quad_grad,
    quad_grad_descent,
    quad_coordinate,
    quad_coordinate_exact,
)

# changer en "True" si LaTeX est bien installé.
plt.rcParams.update(
    {"text.usetex": False, "text.latex.preamble": r"\usepackage{amsmath}"}
)


minv = -5.1
maxv = 5.1

X1, X2 = np.meshgrid(np.linspace(minv, maxv, 50), np.linspace(minv, maxv, 50))
Z = quad(np.array([X1, X2]), theta=0, sig1=1, sig2=1)  # Altitude

# %%
fig = plt.figure(figsize=(3, 3))
ax = plt.axes(projection="3d")
ax.plot_surface(
    X1, X2, Z, rstride=1, cstride=1, cmap=cmap_reversed, edgecolor="none"
)
ax.set_xlim(minv, maxv)
ax.set_ylim(minv, maxv)
ax.set_zlim(0, 20)
plt.show()

# %%
res = []


def plot(
    xs=None,
    c=None,
    theta=np.pi,
    sig1=1,
    sig2=1,
    step_size=1.0,
    max_iter=10,
    levels=(0, 1000),
    xyranges=5.0,
    algos=["GD"],
    colors=["red"],
    markers=["o"],
    **kwargs,
):
    global cbar
    X1, X2 = np.meshgrid(
        np.linspace(-xyranges, xyranges, 50),
        np.linspace(-xyranges, xyranges, 50),
    )
    Z = quad(np.array([X1, X2]), theta=theta, sig1=sig1, sig2=sig2)

    ax.set_xlim(-xyranges, xyranges)
    ax.set_ylim(-xyranges, xyranges)

    if xs is not None:
        if c is not None and len(c) > 0:
            for elem in c:
                if isinstance(elem, matplotlib.collections.PathCollection):
                    elem.remove()
                elif isinstance(elem, matplotlib.contour.QuadContourSet):
                    for coll in elem.collections:
                        coll.remove()
                else:
                    for handle in elem:
                        handle.remove()
        im = ax.contourf(
            X1,
            X2,
            Z,
            levels=np.linspace(
                min(levels[:]) - 1e-3, max(levels[:]) + 1e-3, 30
            ),
            cmap=cmap_reversed,
        )
        try:
            cbar.remove()
        except NameError:
            pass
        cbar = fig.colorbar(im, ax=ax)
        all_c = []
        for idx, xs_ in enumerate(xs):
            x1, x2 = np.array(xs_, dtype="object").T  # deprecated ow
            c1 = ax.plot(
                x1,
                x2,
                color=colors[idx],
                label=f"Trajectoire {algos[idx]}",
                zorder=1,
                alpha=0.8,
                lw=2,
            )
            c2 = ax.scatter(
                x1,
                x2,
                color=colors[idx],
                marker=markers[idx],
                label=f"Itérés {algos[idx]}",
                alpha=0.8,  # 0.5 + 0.5 * np.arange(max_iter) / max_iter,
                zorder=4,
                s=18,
                edgecolors=None,
            )
            all_c.extend([c1, c2])
        c3 = ax.plot(
            x0[0],
            x0[1],
            "X",
            color="w",
            markersize=6,
            zorder=5,
            label="Init. (click!)",
            markeredgewidth=0.1,
            markerfacecolor="k",
            markeredgecolor=(0.5, 0.5, 0.5, 1),
        )

        ax.set_xlim(-xyranges, xyranges)
        ax.set_ylim(-xyranges, xyranges)
        handles, labels = ax.get_legend_handles_labels()
        by_label = dict(zip(labels, handles))
        ax.legend(
            by_label.values(),
            by_label.keys(),
            loc="upper center",
            bbox_to_anchor=(0.5, 1.04999),
            ncol=2,
            fancybox=True,
            shadow=True,
            fontsize=6,
        )
        return [*all_c, c3, im]
    return []


# %%

fig = plt.figure(
    figsize=(4.0, 3.5),
)
ax = plt.gca()
ax.set_aspect("equal")
if plt.rcParams["text.usetex"]:
    plt.title(
        "Lignes de niveau, étapes de descente \n pour la fonction  $x \mapsto x^\\top M x $\noù  $M=\\begin{pmatrix}\\cos(\\theta) & -\\sin(\\theta)\\\\    \\sin(\\theta) & \\cos(\\theta) \\end{pmatrix}  \\begin{pmatrix}\\sigma_1 &   0\\\\0& \\sigma_2\\end{pmatrix}   \\begin{pmatrix}\\cos(\\theta) & -\\sin  (\\theta) \\\\  \\sin(\\theta) & \\cos(\\theta)\\end{pmatrix}^{\\top}$\n",
        fontsize=8,
    )
else:
    plt.title(
        "Lignes de niveau,\n étapes de descente pour la fonction: \n"
        r"$x \mapsto  x^T M x $",
        fontsize=8,
    )
plt.tight_layout()
ax.plot(
    0,
    0,
    marker="P",
    color="w",
    markersize=6,
    zorder=5,
    label="Optimum",
    markeredgewidth=0.1,
    markerfacecolor="w",
    markeredgecolor=(0.5, 0.5, 0.5, 1),
)
x0 = np.array([3.0, 2.0])

out = widgets.Output()


@out.capture(wait=True)
def grad_descent_plot(_):
    global res, controls, all_widg
    fdescent = all_widg["fdescent"].value
    for method in all_widg["fdescent"].options:
        if method not in fdescent:
            all_widg[f"step_size_{method}"].layout.display = "none"
        else:
            all_widg[f"step_size_{method}"].layout.display = "flex"
    kwargs = {}
    for key, val in all_widg.items():
        kwargs[key] = val.value
    if len(fdescent) == 0:
        fdescent = "GD"
    xs, colors, markers = [], [], []
    for idx, method in enumerate(fdescent):
        step_size = all_widg[f"step_size_{method}"].value
        xs.append(dic_optim_algos[method][0](x0, step_size, **kwargs))
        colors.append(dic_optim_algos[method][1])
        markers.append(dic_optim_algos[method][2])
    res = plot(
        xs,
        res,
        algos=fdescent,
        colors=colors,
        markers=markers,
        **kwargs,
    )


def trigger():
    """Trigger refresh using the Zoom"""
    global controls
    controls.children[-1].value = (
        controls.children[-1].value * 1.00001
    )  # trigger refresh on Zoom


def on_click(event):
    global x0, controls
    if event.inaxes is not None:
        x0[0] = event.xdata
        x0[1] = event.ydata
    trigger()


layout = dict(
    # font_style="italic",
    # font_weight="bold",
    height="12px",
    # width="400px",
    width="85%",
    text_color="k",
    align_content="center",
    # min_width="80%",
    margin="6px 50px 10px 10px",
    display="flex",
)
style = {"description_width": "35%"}
layout_hidden = {**layout, "display": "none"}


dic_optim_algos = {
    "GD": (
        quad_grad_descent,
        "red",
        "o",
        FloatSlider(
            value=0.2,
            min=0.0,
            max=0.4,
            step=0.001,
            continuous_update=False,
            description="Pas GD",
            layout=layout_hidden,
            style=style,
        ),
    ),
    "CD": (
        quad_coordinate,
        "orange",
        "d",
        FloatSlider(
            value=0.2,
            min=0.0,
            max=0.4,
            step=0.001,
            continuous_update=False,
            description="Pas CD",
            layout=layout_hidden,
            style=style,
        ),
    ),
    "CDExact": (
        quad_coordinate_exact,
        "yellow",
        "X",
        FloatSlider(
            value=0.2,
            min=0.0,
            max=0.4,
            step=0.001,
            continuous_update=False,
            description="Pas CD (NA)",
            layout=layout_hidden,
            style=style,
        ),
    ),
}
algos = list(dic_optim_algos.keys())


all_widg = dict(
    fdescent=SelectMultiple(
        options=algos,
        value=[algos[0]],
        description="Algorithm",
        disabled=False,
        style=style,
        layout={**layout, "height": "60px"},
    ),
    step_size_GD=dic_optim_algos["GD"][3],
    step_size_CD=dic_optim_algos["CD"][3],
    step_size_CDExact=dic_optim_algos["CDExact"][3],
    max_iter=IntSlider(
        value=5,
        min=0,
        max=100,
        step=1,
        continuous_update=False,
        layout=layout,
        description="Itérations",
        style=style,
    ),
    theta=FloatSlider(
        value=0,
        min=0.0,
        max=2 * np.pi,
        step=2 * np.pi / 20,
        description="θ",  # "$\\theta$",
        continuous_update=False,
        layout=layout,
        style=style,
    ),
    sig1=FloatSlider(
        value=5,
        min=-10.0,
        max=10.0,
        step=0.1,
        continuous_update=False,
        description="σ₁",  # "$\\sigma_1$",
        layout=layout,
        style=style,
    ),
    sig2=FloatSlider(
        value=1,
        min=-10.0,
        max=10.0,
        step=0.1,
        continuous_update=False,
        description="σ₂",  # "$\\sigma_2$",
        layout=layout,
        style=style,
    ),
    levels=FloatRangeSlider(
        value=(0, 200),
        min=-1000,
        max=1000,
        step=20,
        description="Lignes de niveau",
        continuous_update=False,
        layout=layout,
        style=style,
    ),
    xyranges=FloatSlider(
        value=5.0,
        min=0.01,
        max=100,
        step=0.1,
        description="Zoom",
        continuous_update=False,
        layout=layout,
        style=style,
    ),
)

for widget_ in all_widg.values():
    widget_.observe(grad_descent_plot, names="value")

controls = widgets.VBox(list(all_widg.values()))
cid = fig.canvas.mpl_connect("button_press_event", on_click)
trigger()  # init the plot
display.display(widgets.VBox([controls, out]))
plt.show()
# %%
