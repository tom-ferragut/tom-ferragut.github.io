# %%
from sklearn import linear_model
import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np
import seaborn as sns

etudiant = False

sns.set()


# Whole dataset: https://data.iowa.gov/api/views/m3tr-qhgy/rows.csv?accessType=DOWNLOAD
# dataset info: https://data.iowa.gov/Sales-Distribution/Iowa-Liquor-Sales/m3tr-qhgy

url = "http://tanglef.github.io/_teachings/data/HAX606X_optim/datasets/Iowa_Liquor_tp.csv"
path_file = os.path.dirname(__file__)
# path_data = os.path.join(path_file, "datasets", "Iowa_Liquor_tp.csv")


# preprocess with whole dataset
# cols = ["Date", "Bottles Sold"]
# df = pd.read_csv(path_data, usecols=cols, low_memory=True)
# df["month"] = pd.DatetimeIndex(df["Date"]).month
# df["year"] = pd.DatetimeIndex(df["Date"]).year
# df["day"] = pd.DatetimeIndex(df["Date"]).day

# df_plot = df.groupby(["year", "month"], as_index=False)["Bottles Sold"].sum()
# data = df_plot.set_index(
#     pd.to_datetime(df_plot[["year", "month"]].assign(day=1))
# )["Bottles Sold"]


data = pd.read_csv(url)
data.rename(columns={"Unnamed: 0": "Date"}, inplace=True)

y = data["Bottles Sold"].values.reshape(-1, 1)
x = np.arange(len(y)).reshape(-1, 1)

lm = linear_model.LinearRegression()
lm.fit(x, y)
predictions = lm.predict(x)


x2 = np.sin(2 * np.pi / 6 * x)
x3 = np.cos(2 * np.pi / 6 * x)
X = np.hstack((np.ones_like(x), x, x2, x3))

lm_period = linear_model.LinearRegression(fit_intercept=False)
lm_period.fit(X, y)
predictions_period = lm_period.predict(X)

if not etudiant:
    directory = "prebuiltimages"
    path_images = os.path.join(path_file, directory)
    if not os.path.isdir(path_images):
        os.mkdir(directory)


# Figure 1: raw data
fig, ax = plt.subplots(1, 1, figsize=(7, 5))

data.plot(
    "Date",
    "Bottles Sold",
    color="b",
    title="Monthly alcool sales (Iowa, USA)",
    ax=ax,
    linewidth=1,
)
_ = ax.set_xlabel("Date")
_ = ax.set_ylabel("Bottles Sales")
ax.xaxis.set_tick_params(rotation=50)
ax.legend()
plt.tight_layout()
plt.show()
if not etudiant:
    fig.savefig(os.path.join(path_images, "raw.pdf"))


# Figure 2: raw data + least squares
fig, ax = plt.subplots(1, 1, figsize=(7, 5))

data.plot(
    "Date",
    "Bottles Sold",
    color="b",
    title="Monthly alcool sales (Iowa, USA)",
    ax=ax,
    linewidth=1,
)
_ = ax.set_xlabel("Date")
_ = ax.set_ylabel("Bottles Sales")
ax.plot(data["Date"], predictions, lw=3, label="Least squares", color="r")
ax.xaxis.set_tick_params(rotation=50)
ax.legend()
plt.tight_layout()
plt.show()
if not etudiant:
    fig.savefig(os.path.join(path_images, "raw_ols.pdf"))


# Figure 3: raw data + least squares + least squares (with periodicity)
fig, ax = plt.subplots(1, 1, figsize=(7, 5))
data.plot(
    "Date",
    "Bottles Sold",
    color="b",
    title="Monthly alcool sales (Iowa, USA)",
    ax=ax,
    linewidth=1,
)
_ = ax.set_xlabel("Date")
_ = ax.set_ylabel("Bottles Sales")
ax.plot(data["Date"], predictions, lw=3, label="Least squares", color="r")
ax.plot(
    data["Date"],
    predictions_period,
    label="Least squares (with periodicity)",
    color="k",
)
ax.xaxis.set_tick_params(rotation=50)
ax.legend()
plt.tight_layout()
plt.show()
if not etudiant:
    fig.savefig(os.path.join(path_images, "raw_ols_ols_w_period.pdf"))

# %%
