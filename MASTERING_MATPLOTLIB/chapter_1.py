import matplotlib
matplotlib.use('nbagg')


import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.backends import backend_agg
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.gridspec import GridSpec
import seaborn as sns
from IPython.display import Image


pallete_name = "husl"
colors = sns.color_palette(pallete_name, 8)
colors.reverse()
cmap = mpl.colors.LinearSegmentedColormap.from_list(
    pallete_name, colors)


colors
