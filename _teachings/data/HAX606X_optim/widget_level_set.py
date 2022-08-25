# %%
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
from scipy.stats import norm, multivariate_normal

from ipywidgets import interactive, fixed, FloatRangeSlider, FloatSlider, Label

from dico_math_functions import (
    quad,
    quad_grad,
    quad_grad_descent,
    quad_coordinate,
)

# True si latex est bien installé
plt.rcParams.update(
    {"text.usetex": False, "text.latex.preamble": r"\usepackage{amsmath}"}
)


# minv = -5.1
# maxv = 5.1
# theta, sig1, sig2 = np.pi, 1, 1
# Sigma = angle_scalar_to_covmat(theta, sig1, sig2)

# X1, X2 = np.meshgrid(np.linspace(minv, maxv, 50), np.linspace(minv, maxv, 50))
# Z = quad(np.array([X1, X2]), Sigma=Sigma)  # Altitude
# # Z = f(np.array([X1, X2]))  # Altitude


# %%
# set up a figure twice as wide as it is tall
fig = plt.figure(figsize=(5.5, 3))
ax1 = fig.add_subplot(1, 2, 1, projection="3d")
ax2 = fig.add_subplot(1, 2, 2)

if plt.rcParams["text.usetex"]:
    fig.suptitle(
        "Lignes de niveau \n pour la fonction  $x \mapsto x^\\top M x $\noù  $M=\\begin{pmatrix}\\cos(\\theta) & -\\sin(\\theta)\\\\    \\sin(\\theta) & \\cos(\\theta) \\end{pmatrix}  \\begin{pmatrix}\\sigma_1 &   0\\\\0& \\sigma_2\\end{pmatrix}   \\begin{pmatrix}\\cos(\\theta) & -\\sin  (\\theta) \\\\  \\sin(\\theta) & \\cos(\\theta)\\end{pmatrix}^{\\top}$\n",
        fontsize=8,
    )
else:
    fig.suptitle(
        r"Lignes de niveau pour la fonction:  $x \mapsto x^T M x$",
        fontsize=8,
    )
cbar = None
plt.tight_layout()
plt.show()


def level_sets_plot(theta, sig1, sig2):
    global ax1, ax2, cbar
    im2 = None
    minv = -5.0
    maxv = 5.0
    # theta, sig1, sig2 = np.pi, 1, 1
    # Sigma = angle_scalar_to_covmat(theta, sig1, sig2)

    X1, X2 = np.meshgrid(
        np.linspace(minv, maxv, 50), np.linspace(minv, maxv, 50)
    )
    Z = quad(np.array([X1, X2]), theta, sig1, sig2)
    for l in [ax1, ax2]:
        l.remove()
    if im2 is not None:
        #         cbar.remove()
        # if isinstance(im2, matplotlib.contour.QuadContourSet):
        for coll in im2.collections:
            coll.remove()

    # ===============
    #  First subplot
    # ===============
    # set up the axes for the first plot
    ax1 = fig.add_subplot(1, 2, 1, projection="3d")

    ax1.plot_surface(
        X1, X2, Z, rstride=1, cstride=1, cmap=cmap_reversed, edgecolor="none"
    )

    ax1.set_xlim(minv, maxv)
    ax1.set_ylim(minv, maxv)
    ax1.set_zlim(0, 100)

    # ===============
    # Second subplot
    # ===============
    # set up the axes for the second plot
    ax2 = fig.add_subplot(1, 2, 2)
    im2 = ax2.contourf(
        X1,
        X2,
        Z,
        levels=30,
        cmap=cmap_reversed,
    )
    if cbar is not None:
        cbar.remove()
    cbar = fig.colorbar(im2, ax=ax2)
    ax2.set_xlim(-5, 5)
    ax2.set_ylim(-5, 5)
    return ax1, ax2, im2
    plt.tight_layout()
    ax2.set_aspect(1)


interactive(
    level_sets_plot,
    theta=FloatSlider(
        value=0,
        min=0.0,
        max=2 * np.pi,
        step=2 * np.pi / 20,
        description="θ",  # "$\\theta$",
    ),
    sig1=FloatSlider(
        value=5,
        min=-10.0,
        max=10.0,
        step=0.1,
        continuous_update=False,
        description="σ₁",  # "$\\sigma_1$",
    ),
    sig2=(
        FloatSlider(
            value=1,
            min=-10.0,
            max=10.0,
            step=0.1,
            continuous_update=False,
            description="σ₂",  # "$\\sigma_2$",
        )
    ),
)
