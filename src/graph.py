import matplotlib
import matplotlib.pyplot as plt

import flet as ft
from flet.matplotlib_chart import MatplotlibChart

import numpy as np

matplotlib.use("svg")

def graph(page: ft.Page):
    dt = 0.01
    t = np.arange(0, 30, dt)
    nse1 = np.random.randn(len(t))  
    nse2 = np.random.randn(len(t))  

    s1 = np.sin(2 * np.pi * 10 * t) + nse1
    s2 = np.sin(2 * np.pi * 10 * t) + nse2

    fig, axs = plt.subplots(2, 1)
    axs[0].plot(t, s1, t, s2)
    axs[0].set_xlim(0, 2)
    axs[0].set_xlabel("test")
    axs[0].set_ylabel("test")
    axs[0].grid(True)

    cxy, f = axs[1].cohere(s1, s2, 256, 1.0 / dt)
    axs[1].set_ylabel("test")

    fig.tight_layout()

    page.add(MatplotlibChart(fig, expand=True))

    fig, ax = plt.subplots()

    fruits = ["apple", "blueberry", "cherry", "orange"]
    counts = [40, 100, 190, 55]
    bar_labels = ["red", "blue", "_red", "orange"]
    bar_colors = ["tab:red", "tab:blue", "tab:red", "tab:orange"]

    ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

    ax.set_ylabel("fruit supply")
    ax.set_title("Fruit supply by kind and color")
    ax.legend(title="Fruit color")

    page.add(MatplotlibChart(fig, expand=True))
    
ft.app(target = graph)