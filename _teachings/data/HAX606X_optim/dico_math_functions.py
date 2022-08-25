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

from scipy.optimize import minimize
from ipywidgets import interactive, fixed, FloatRangeSlider, FloatSlider, Label


@njit
def g(x):
    x1, x2 = x[0], x[1]
    return (x1 ** 2 + x2 - 11) ** 2 + (x1 + x2 ** 2 - 7) ** 2


@njit
def h(x):
    x1, x2 = x[0], x[1]
    return x1 ** 4 + x2 ** 4 - 4 * (x1 - 1) ** 2 - (x2 - 1) ** 2 + 1


@njit
def h_grad(x):
    x1, x2 = x
    df_x1 = 4 * x1 ** 3 - 8 * (x1 - 1)
    df_x2 = 4 * x2 ** 3 - 2 * (x2 - 1)
    return np.array([df_x1, df_x2])


@njit
def g_grad(x):
    x1, x2 = x
    df_x1 = 2 * (-7 + x1 + x2 ** 2 + 2 * x1 * (-11 + x1 ** 2 + x2))
    df_x2 = 2 * (-11 + x1 ** 2 + x2 + 2 * x2 * (-7 + x1 + x2 ** 2))
    return np.array([df_x1, df_x2])


@njit
def f(x):
    x1, x2 = x[0], x[1]
    return (x1 - 1) ** 2 + 3 * (x2 + 1) ** 2


@njit
def f_grad(x):
    x1, x2 = x
    df_x1 = 2 * (x1 - 1)
    df_x2 = 6 * (x2 + 1)
    return np.array([df_x1, df_x2])


@njit
def covmat_to_scalar(Sigma):
    """Convert covariance matrix to scalars."""
    sigmax = np.sqrt(Sigma[0, 0])
    sigmay = np.sqrt(Sigma[1, 1])
    sigmaxy = Sigma[1, 0]
    return sigmax, sigmay, sigmaxy


@njit
def angle_scalar_to_covmat(theta, sig1, sig2):
    """Inverse function of the previous one."""
    rotation = np.zeros((2, 2))
    rotation[0, 0] = np.cos(theta)
    rotation[1, 0] = np.sin(theta)
    rotation[0, 1] = -np.sin(theta)
    rotation[1, 1] = np.cos(theta)
    Sigma = rotation @ np.array([[sig1, 0.0], [0.0, sig2]]) @ rotation.T
    return Sigma


# theta, sig1, sig2 = np.pi, 10, 10
# Sigma = angle_scalar_to_covmat(theta, sig1, sig2)


@njit
def quad(x, theta=0, sig1=1, sig2=1):
    Sigma = angle_scalar_to_covmat(theta, sig1, sig2)
    x1, x2 = x[0], x[1]
    return (
        x1 ** 2 * Sigma[0, 0]
        + x2 ** 2 * Sigma[1, 1]
        + 2.0 * Sigma[1, 0] * x1 * x2
    ) / 2.0
    #  x.T @ Sigma @ x


@njit
def quad_grad(x, theta=0, sig1=1, sig2=1):
    Sigma = angle_scalar_to_covmat(theta, sig1, sig2)
    x1, x2 = x[0], x[1]
    df_x1 = x1 * Sigma[0, 0] + Sigma[1, 0] * x2
    df_x2 = x2 * Sigma[1, 1] + Sigma[1, 0] * x1
    return np.array([df_x1, df_x2])


@njit
def grad_descent(x0, step_size, max_iter=10, f=f, f_grad=f_grad):
    """Gradient descent with constant step size"""
    x = x0
    xs = [x]
    for k in range(max_iter):
        d_k = -f_grad(x)  # direction of descent
        t_k = step_size  # does not depend on k
        x = x + step_size * d_k
        xs.append(x)
        print(f(x))
    return xs


def quad_grad_descent(
    x0,
    step_size,
    max_iter=10,
    theta=np.pi,
    sig1=10.0,
    sig2=1.0,
    levels=2500,
    xyranges=5,
    **kwargs,
):
    """Gradient descent with constant step size"""
    x = x0
    xs = [x]
    for k in range(max_iter):
        d_k = -quad_grad(
            x, theta=theta, sig1=sig1, sig2=sig2
        )  # direction of descent
        x = x + step_size * d_k  # a copy is performed of x
        xs.append(x)
        # print(quad(x, Sigma=Sigma))
    return xs


def quad_coordinate(
    x0,
    step_size,
    max_iter=10,
    theta=np.pi,
    sig1=10.0,
    sig2=1.0,
    levels=2500,
    xyranges=5,
    **kwargs,
):
    """Coordinate descent with constant step size"""
    x = x0.copy()
    xs = [x.copy()]
    for k in range(max_iter):
        for j in range(2):  # 2D plots
            d_k = -quad_grad(x, theta=theta, sig1=sig1, sig2=sig2)[
                j
            ]  # direction of descent
            t_k = step_size  # does not depend on k
            x[j] = x[j] + step_size * d_k
            xs.append(x.copy())
    return xs


def quad_coordinate_exact(
    x0,
    step_size,
    max_iter=10,
    theta=np.pi,
    sig1=10.0,
    sig2=1.0,
    levels=2500,
    xyranges=5,
    **kwargs,
):
    """Coordinate descent with optimized step size"""
    x = x0.copy()
    xs = [x.copy()]
    Id = np.eye(2)
    for k in range(max_iter):
        for j in range(2):  # 2D plots
            d_k = -quad_grad(x, theta=theta, sig1=sig1, sig2=sig2)[
                j
            ]  # direction of descent

            def f(t_k):
                return quad(
                    x + t_k * d_k * Id[j], theta=theta, sig1=sig1, sig2=sig2
                )

            res = minimize(f, 0.0)
            # print(res.x)
            x[j] = x[j] + res.x * d_k
            xs.append(x.copy())
    return xs
