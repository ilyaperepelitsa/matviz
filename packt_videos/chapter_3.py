from IPython.display import display_png
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure

first_set = pd.read_csv("~/quant/fastest_routes_train_part_1.csv")
second_set = pd.read_csv("~/quant/fastest_routes_train_part_2.csv")
total_set = pd.concat([first_set, second_set])

total_set.
def explode(df, lst_cols, fill_value=''):
    # make sure `lst_cols` is a list
    if lst_cols and not isinstance(lst_cols, list):
        lst_cols = [lst_cols]
    # all columns except `lst_cols`
    idx_cols = df.columns.difference(lst_cols)

    # calculate lengths of lists
    lens = df[lst_cols[0]].str.len()

    if (lens > 0).all():
        # ALL lists in cells aren't empty
        return pd.DataFrame({
            col:np.repeat(df[col].values, df[lst_cols[0]].str.len())
            for col in idx_cols
        }).assign(**{col:np.concatenate(df[col].values) for col in lst_cols}) \
          .loc[:, df.columns]
    else:
        # at least one list in cells is empty
        return pd.DataFrame({
            col:np.repeat(df[col].values, df[lst_cols[0]].str.len())
            for col in idx_cols
        }).assign(**{col:np.concatenate(df[col].values) for col in lst_cols}) \
          .append(df.loc[lens==0, idx_cols]).fillna(fill_value) \
          .loc[:, df.columns]

total_exploded = explode(total_set, ["street_for_each_step", "distance_per_step", "travel_time_per_step"
                   , "step_maneuvers", "step_direction", "step_location_list"])
total_exploded.shape

latlon = pd.DataFrame(total_exploded.step_location_list.str.split(',',1).tolist(),
                                   columns = ['lon','lat'])
total_exploded = pd.concat([total_exploded, latlon], axis=1, join='inner')
total_exploded.shape
