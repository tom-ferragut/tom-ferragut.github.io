# %%
"""
=========================================================
                            TP1
Prise en main des outils pour l'optimisation avec Python
==========================================================
"""
# %%
# Import des packages nécessaires pour ce TP
import time
import numpy as np
import matplotlib.pyplot as plt


# %%
# Cellule
1 + 3  # commentaire en ligne

# %%
###############################################################################
# # Question(Dépassement)
###############################################################################
# Rem: noqa = no quality assurance
import sys  # noqa

# %%

n_max = ...  # XXX TODO
print(n_max)
np.testing.assert_almost_equal(n_max + 1, n_max)
test = ... == ...
print(f"n_max est égal à n_max + 1 ? C'est {test}, mais bizarre")
print(n_max * ...)
print(...)

# %%
###############################################################################
# # Question(Soupassement)
###############################################################################
# La fonction `range` permet de générer tous les entiers entre deux valeurs
# par défaut, elle commence à 0 et a un pas de 1.

print(list(range(6)))

# Pour aller chercher des ordres de grandeur extrême il est pratique
# d'utiliser une grille géométrique avec np.logspace.

n_petit = 1200
n_petits = np.logspace(-n_petit, 0, base=2, num=n_petit + 1)
print(n_petits)
print(n_petits[::-1])

for idx, val in enumerate(n_petits[::-1]):
    print(idx, val)
    if val == ...:  # XXX TODO
        break
print(idx, val)

# %%
###############################################################################
# # Question(Arrondis):
###############################################################################

print(10 ** 9 == 10 ** 9 + 10 ** (-8))
print(10 ** 9, 10 ** 9 + 10 ** (-8))

print(10 ** 9 == 10 ** 9 + 10 ** -7)
print(10 ** 9, 10 ** 9 + 10 ** -7)

print(10 ** 9 == 10 ** 9 + np.spacing(10 ** 9) / 2)
print(10 ** 9, 10 ** 9 + np.spacing(10 ** 9) / 2)

print(10 ** 9 == 10 ** 9 + np.spacing(10 ** 9) / 1.9)
print(10 ** 9, 10 ** 9 + np.spacing(10 ** 9) / 1.9)

print(0.6 == 0.3 + 0.2 + 0.1)
print(0.6, 0.3 + 0.2 + 0.1)

print(0.6 == 0.1 + 0.2 + 0.3)
print(0.6, 0.1 + 0.2 + 0.3)

# %%
###############################################################################
# # Question(Précision relative / absolue)
###############################################################################

# https://docs.python.org/3/tutorial/floatingpoint.html

help(np.isclose)
np.isclose(0.6, 0.1 + 0.2, +0.3, atol=..., rtol=...)  # XXX TODO


# %%
# Rappels (ou pas) sur les matrices et vecteurs
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# %%
###############################################################################
# Question(Algèbre linéaire)
###############################################################################
# Une matrice est seulement une liste de listes (une par ligne) en `numpy`.


# Somme de deux vecteurs
A = np.array([1.0, 2, 3])
B = np.array([-1, -2, -3.0])

# Attribuer à la variable C la somme de A et B
sum_A_B = ...  # XXX TODO

np.testing.assert_almost_equal(np.zeros((3,)), sum_A_B)
print("it worked")

# %%
# Le produit terme à terme avec *
prod_A_B = ...  # XXX TODO

np.testing.assert_almost_equal(np.array([-1.0, -4, -9]), prod_A_B)
print("it worked")

# Remarque: la même chose fonctionne terme à terme avec \, ** (puissance)
np.testing.assert_almost_equal(np.array([1.0, 4, 9]), A ** 2)
print("it worked: even for powers")


# Le produit scalaire (ou matriciel) est l'opérateur @
J = np.array([[0, 0, 1.0], [1.0, 0, 0], [0, 1.0, 0]])

I3 = np.eye(3)

# Verifier que J^3 = Id de deux facons.
np.testing.assert_almost_equal(I3, ...)  # XXX TODO
print("it worked: method 1")
np.testing.assert_almost_equal(I3, ...)  # XXX TODO
print("it worked: method 2")


# %%
# # Opérations et affichage de résultats dans une f-string
# ## L'inversion matricielle

# Dans les accolades ci-dessous, effectuer les opérations associées
# ajouter un = juste avant de fermer l'accolade: qu'est-ce-que cela change ?  # XXX TODO

print(f"L'inverse de la matrice: \n {J} \n est \n {np.linalg.inv(J)}")

# REMARQUE: en pratique on n'utilisera jamais cette fonction!
# En effet, on n'inverse **JAMAIS JAMAIS JAMAIS** une matrice,
# sauf si l'on a une bonne raison de le faire.
# La plupart du temps on doit résoudre un système lineaire Ax = b,
# et il n'est pas utile de calculer A^{-1}b pour cela.

n = 20  # XXX TODO: tester avec n=100
Jbig = np.roll(np.eye(n), -1, axis=1)  # matrice de permutation de taille n
print(Jbig)

b = np.arange(n)
print(b)

# Résolution de système par une méthode naive: inversion de matrice
t0 = time.perf_counter()  # XXX TODO
y1 = ... @ b
timing_naive = ...
print(
    f"Temps pour résoudre un système avec la formule mathématique: {timing_naive:.4f} s."
)

# Résolution de système par une méthode adaptée: fonctions dédiée de `numpy``
# XXX TODO
y2 = ...
timinig_optimized = ...
print(
    f"Temps pour résoudre un système avec la formule mathématique: {timing_optimized:.4f} s.\nC'est donc {timing_naive / timing_optimized} fois plus rapide d'utiliser la seconde formulation"
)

np.testing.assert_almost_equal(y1, y2)
print("Les deux méthodes trouvent le même résultat")


# REM: Pour des comparaisons d'efficacité temporelle plus poussées on pourra utiliser le package `timeit`` https://docs.python.org/3/library/timeit.html


# ## Le slicing
# Cela permet d'extraire des éléments selon un critère (position, condition)
# `:` signifie "tout le monde"
# `0` en première (resp deuxième) position signifie la première ligne (resp colonne)
print(f"The first column is {A[:, 0]}")

# Afficher la deuxième ligne de A
print(f"The second row is {...}")  # XXX TODO


# Mettre à zero une ligne sur deux de la matrice identité de taille 5 x 5.

C = np.eye(5, 5)
# C[,] = 0  # mettre à zéro une ligne sur deux. # XXX TODO


# ## Grilles de nombres
# Grille linéaire:
# La fonction linspace du package numpy permet de générer une grille de points
# entre deux valeurs de manière linéaire, sa syntaxe est:
#               np.linspace(val1, val2, num=<nombre de points>)
# Associer à x une grille de 100 points entre -5 et 5

x = ...  # XXX TODO
print(x)

# Grille géométrique:
np.logspace(..., ..., num=9)  # XXX TODO


# %% Tout numpy array a un tuple associé de ses dimensions
# La dimension est appelée à l'aide de l'attribut `shape`.
# Pour accéder à l'attribut d'un object, on utilise la syntaxe `.<nom_attribut>`

d = np.arange(6)
# XXX TODO

# %%
###############################################################################
# # Question(Affichage de fonctions 1D)
###############################################################################

# XXX TODO
x = np.linspace(...)
y = ...

plt.figure(figsize=(8, 6))
plt.plot(x, y, label=r"$f:x\mapsto \cos(x)$", zorder=1)
plt.hlines(
    y=...,
    xmin=...,
    xmax=...,
    label=r"$\pm 1$",
    color="r",
    zorder=1,
    linestyles="dotted",
)
plt.hlines(...)

x_extrema = np.pi * np.arange(-3, 4)
y_extrema = np.cos(x_extrema)

plt.scatter(..., s=...)
plt.xlabel(...)
plt.ylabel(...)
plt.legend()
plt.title(...)
plt.tight_layout()
plt.show()


# %%
###############################################################################
# # Question(Graphes multiples)
###############################################################################
# Lise de couleurs, dégradé de violet:
colors = plt.cm.Purples(np.linspace(0.3, 1, 5))
lambdas = np.arange(1, 6)
x = np.linspace(0, 10, 1000, endpoint=True)

fig, axs = plt.subplots(..., ..., sharex=True, figsize=(6, 8))


for i in range(...):
    y = np.exp(-x * ...)
    axs[0].plot(x, y, label=..., color=...)  # XXX TODO
    axs[1].semilogy(...)

# Add subtitles / titles
fig.suptitle("Décroissance exponentielle")
axs[0].set_title("Échelle classique")
axs[1].set_title("Échelle semi-logarithmique")
axs[1].legend(loc=3)

# Pour aller plus loin: # XXX TODO
# import matplotlib.ticker as ticker  # noqa

# def mimic_ticks(x, _):
#     return fr'$10^{{{x:.0f}}}$'


# # Afficher les valeurs sur l'axe y en puissances de 10
# axs[2].yaxis.set_major_formatter(ticker.FuncFormatter(mimic_ticks))
# plt.tight_layout()

# %%
###############################################################################
# # Question(Conditions du premier et deuxième ordre):
###############################################################################

# Créer une grille de points avec meshgrid: exemple

x = np.linspace(-5, 10, 15)
y = np.linspace(0, 20, 10)
xx, yy = np.meshgrid(x, y)

# xx est x répété "le nombre de points dans y" fois sur les lignes
# yy est y répété "le nombre de points dans x" fois sur les colonnes

plt.figure()
plt.plot(xx, yy, ls="None", marker=".")
plt.show()

# Une fonction à deux variables pourra ainsi être visualisée en l'évaluant
# sur chacun des points d'une grille assez fine.

# %%
# Il faut changer l'option d'affichage pour que l'on puisse utiliser une
# interactivement la figure 3D et la visualiser sous tous les angles possibles.
# Pour cela lancer:
from IPython import get_ipython  # noqa

get_ipython().run_line_magic("matplotlib", "widget")

# Alternative: taper
# % matplotlib widget
# dans l'invite de commande.


# Gestion de la colorbar
from pylab import cm  # noqa:E402
from mpl_toolkits.mplot3d import Axes3D

def f(x, y):
    return x ** 2 - y ** 4


x = np.arange(-1, 1, 0.05)
y = np.arange(-1, 1, 0.05)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)


fig_level_set, ax1 = plt.subplots(1, 1, figsize=(3, 3))
im = ax1.contourf(X, Y, Z, levels=30, cmap="RdBu_r")
cbar = fig_level_set.colorbar(im, ax=ax1, fraction=0.046, pad=0.04)

ax1.set_title(r"$x^2 - y^4$")

fig_surface = plt.figure(figsize=(3, 3))
ax2 = fig_surface.add_subplot(1, 1, 1, projection="3d")
surf = ax2.plot_surface(
    X,
    Y,
    Z,
    rstride=1,
    cstride=1,
    cmap=cm.RdBu_r,
    linewidth=0,
    antialiased=False,
    alpha=0.8,
)
# XXX TODO
ax1.scatter(..., alpha=..., zorder=2)
ax2.scatter(...)
plt.show()

# %%
###############################################################################
# # Question(Dérivées directionnelles):
###############################################################################


def z(x, y):
    return np.where(np.allclose([x, y], 0), 0, x * y / (x ** 2 + y ** 2))


def dx(x, y):
    return np.where(
        np.allclose([x, y], 0),
        0,
        y * (y ** 2 - x ** 2) / (x ** 2 + y ** 2) ** 2,
    )


def dy(x, y):
    return np.where(
        np.allclose([x, y], 0),
        0,
        x * (x ** 2 - y ** 2) / (x ** 2 + y ** 2) ** 2,
    )


x = np.arange(-0.5, 0.5, 0.01)
y = np.arange(-0.5, 0.5, 0.01)
X, Y = np.meshgrid(x, y)
Z = z(X, Y)

dX = dx(X, Y)
dY = dy(X, Y)
speed = np.sqrt(dX * dX + dY * dY)

fig = plt.figure(figsize=(8, 4))
ax = fig.add_subplot(1, 2, 2)
# im = ax.imshow(Z, cmap=cm.RdBu_r)
im = ax.contourf(X, Y, Z, levels=30, cmap="RdBu_r")  # XXX TODO
ax.streamplot(X, Y, dX, dY, color="k", linewidth=5 * speed / speed.max())
ax.set_xlim([x.min(), x.max()])
ax.set_ylim([y.min(), y.max()])
ax.set_aspect("equal")

cbar = fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)

ax.set_title(r"$\frac{xy}{x^2 + y^2}$")
ax = fig.add_subplot(1, 2, 1, projection="3d")
surf = ax.plot_surface(
    X,
    Y,
    Z,
    rstride=1,
    cstride=1,
    cmap=cm.RdBu_r,
    linewidth=0,
    antialiased=False,
)
# ax = fig.add_subplot(1, 3, 3)

# ax.streamplot(X, Y, dX, dY, color='k', linewidth=5*speed / speed.max())
# ax.set_xlim([x.min(), x.max()])
# ax.set_ylim([y.min(), y.max()])

plt.tight_layout()
plt.show()


fig, ax = plt.subplots(figsize=(4, 4))
CS = ax.contour(X, Y, Z)
ax.clabel(CS, inline=True, fontsize=10)
ax.imshow(
    Z, cmap=cm.RdBu_r, extent=[min(x), max(x), min(y), max(y)], origin="lower"
)
ax.set_title("Alternative")
plt.tight_layout(pad=3.0)
plt.show()

# %%
###############################################################################
# L'aléatoire en Python
###############################################################################

# Pour obtenir des nombres aléatoires, on crée un générateur d'abord
# Créer une matrice (4, 5) iid d'une loi de Laplace d'espérance 0
# et de variance 2

generateur = np.random.default_rng()
M = ...  # XXX TODO
print(M)

# %%
n_samples = 10000
X = np.empty([n_samples, 3])
X[:, 0] = ...
X[:, 1] = ...
X[:, 2] = ...

lois = ["Loi de Gauss", "Loi de Laplace", "Loi de Cauchy"]

fig_hist, ax = plt.subplots(3, 1, figsize=(3, 3))

for i, name in enumerate(lois):
    ax[i].hist(..., bins=100, density=True)
    ax[i].set_title(name)

plt.tight_layout()
# %%
