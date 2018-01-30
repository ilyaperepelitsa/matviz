from IPython.display import display_png
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure



first_set = pd.read_csv("~/quant/fastest_routes_train_part_1.csv")
second_set = pd.read_csv("~/quant/fastest_routes_train_part_2.csv")
total_set = pd.concat([first_set, second_set])


for col in ["street_for_each_step", "distance_per_step", "travel_time_per_step",
                "step_maneuvers", "step_direction", "step_location_list"]:
    total_set.loc[:,col] = total_set.loc[:,col].str.split('|').tolist()
