# from IPython.display import display_png
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
import matplotlib
from scipy import stats

from itertools import cycle
from cycler import cycler
from collections import defaultdict
from random import shuffle

palette = ['#aa4747','#bf7265','#b29563','#54637a','#603f63','#824a53','#54787a',
            '#918e5f','#bf8765','#4e3f63','#824a6b','#547a63','#6b7a54']

palette_pastel = ['#bcc19c','#c19c9e','#c19cbc','#c1a09c','#c19cac','#9c9dc1','#9cb0c1',
            '#c1b19c','#b29cc1','#9cc1bd','#9cc1a2']

plt.rc("axes", prop_cycle = (cycler("color", palette)))


color_cycler = cycle(plt.rcParams["axes.prop_cycle"])
cmap = lambda x: [x, next(color_cycler)["color"]]

labels = []




plt.figure(figsize = (10, 10))




for street in sample_1k["starting_street"].unique():
    labels.append(cmap(street))

for street in labels:
    plt.scatter(sample_1k.loc[sample_1k["starting_street"] == street[0], "lon"],
                sample_1k.loc[sample_1k["starting_street"] == street[0], "lat"],
                c = street[1], alpha = 0.5, edgecolor = "none", linewidth = 0.5)
# pew
legend_handlers = [plt.scatter([], [], marker = "o", label = label_entry[0],
                    edgecolors = label_entry[1], c = 'none') for label_entry in labels]

plt.legend(handles = legend_handlers, scatterpoints = 1, ncol = 3, loc = 'upper center')
plt.axes().set_aspect("equal")
plt.show()

labels = []
sample_trips = np.random.choice(total_exploded["starting_street"].unique(), 3)
sample_1k = total_exploded.loc[total_exploded["starting_street"].isin(sample_trips), :]

for street in sample_1k["starting_street"].unique():
    labels.append(cmap(street))
labels

for i in labels:
    # plt.hist(sample_1k.loc[sample_1k["starting_street"] == i[0], "lon"], color = i[1], histtype = "barstacked", bins = 20)
    print(sample_1k.loc[sample_1k["starting_street"] == i[0], "lon"].shape)
    # print(i)
plt.show()
