# from IPython.display import display_png
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure



# first_set = pd.read_csv("~/quant/fastest_routes_train_part_1.csv")
# second_set = pd.read_csv("~/quant/fastest_routes_train_part_2.csv")
# total_set = pd.concat([first_set, second_set])
#
#
# for col in ["street_for_each_step", "distance_per_step", "travel_time_per_step",
#                 "step_maneuvers", "step_direction", "step_location_list"]:
#     total_set.loc[:,col] = total_set.loc[:,col].str.split('|').tolist()
#
#
# def explode(df, lst_cols, fill_value=''):
#     # make sure `lst_cols` is a list
#     if lst_cols and not isinstance(lst_cols, list):
#         lst_cols = [lst_cols]
#     # all columns except `lst_cols`
#     idx_cols = df.columns.difference(lst_cols)
#
#     # calculate lengths of lists
#     lens = df[lst_cols[0]].str.len()
#
#     if (lens > 0).all():
#         # ALL lists in cells aren't empty
#         return pd.DataFrame({
#             col:np.repeat(df[col].values, df[lst_cols[0]].str.len())
#             for col in idx_cols
#         }).assign(**{col:np.concatenate(df[col].values) for col in lst_cols}) \
#           .loc[:, df.columns]
#     else:
#         # at least one list in cells is empty
#         return pd.DataFrame({
#             col:np.repeat(df[col].values, df[lst_cols[0]].str.len())
#             for col in idx_cols
#         }).assign(**{col:np.concatenate(df[col].values) for col in lst_cols}) \
#           .append(df.loc[lens==0, idx_cols]).fillna(fill_value) \
#           .loc[:, df.columns]
#
#
#
# total_exploded = explode(total_set, ["street_for_each_step", "distance_per_step", "travel_time_per_step"
#                    , "step_maneuvers", "step_direction", "step_location_list"])
#
# latlon = pd.DataFrame(total_exploded.step_location_list.str.split(',',1).tolist(),
#                                    columns = ['lon','lat'])
# total_exploded = pd.concat([total_exploded, latlon], axis=1, join='inner')
#
# total_exploded["latlon"] = total_exploded.loc[:,["lat", "lon"]].apply(lambda x: ', '.join(x), axis=1)
#
#
# total_exploded.info()
#
# total_exploded.to_csv("~/quant/exploded.csv", index = False)


total_exploded = pd.read_csv("~/quant/exploded.csv")


trip_ids = total_exploded["id"].unique()
sample_trips = np.random.choice(trip_ids, 30000)


sample_30k = total_exploded.loc[total_exploded["id"].isin(sample_trips), :]
# sample_30k.head()
plt.hist(sample_30k["distance_per_step"])
plt.show()
plt.hist(sample_30k["travel_time_per_step"])
plt.show()


plt.figure(figsize = (18.5, 10.5))
plt.hist(sample_30k["total_travel_time"])
# plt.gcf().set_size_inches(18.5, 10.5)
# plt.figure(figsize = (18.5, 10.5))
plt.show()


# fig.savefig('test2png.png', dpi=100)



######################################################################################
###########################################
###########################################
# PLOTTING LINES


# sample_trips = np.random.choice(trip_ids, 30000)
plt.figure(figsize = (18.5, 10.5))
for i in range(0, 100):
    # print(i)
    rand_index = np.random.choice(sample_30k["id"].unique(), 1)

    plt.plot(sample_30k.loc[sample_30k["id"].isin(rand_index), "lon"],
                sample_30k.loc[sample_30k["id"].isin(rand_index), "lat"])

# invert_x = plt.xlim()[::-1]
# invert_y = plt.ylim()[::-1]
# invert_y
# plt.xlim(invert_x)
# plt.ylim(invert_y)
plt.savefig('~', dpi=100)
plt.show()
