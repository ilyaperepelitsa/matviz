from IPython.display import display_png
import matplotlib.pyplot as plt
import pandas as pd


from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure



first_set = pd.read_csv("~/quant/fastest_routes_train_part_1.csv")
second_set = pd.read_csv("~/quant/fastest_routes_train_part_2.csv")
