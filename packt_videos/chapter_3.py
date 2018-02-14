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

### Generate a bunch of line graphs and save them
# "".join(np.random.choice(['-', '--', '-.', ':', 'steps'], 1))

# sample_trips = np.random.choice(trip_ids, 30000)
for aspect in ["equal", "auto"]:
    for x in range(1, 5):
        plt.figure(figsize = (18.5, 10.5))

        for i in range(0, 100):
            # print(i)
            rand_index = np.random.choice(sample_30k["id"].unique(), 1)

            plt.plot(sample_30k.loc[sample_30k["id"].isin(rand_index), "lon"],
                        sample_30k.loc[sample_30k["id"].isin(rand_index), "lat"],
                        "".join(np.random.choice(['-', '--', '-.', ':'], 1)))

        # invert_x = plt.xlim()[::-1]
        # invert_y = plt.ylim()[::-1]
        # invert_y
        # plt.xlim(invert_x)
        # plt.ylim(invert_y)
        plt.axes().set_aspect(aspect)
        plt.savefig('/Users/ilyaperepelitsa/quant/taxi_test_{}_{:d}.jpg'.format(aspect, x), dpi=300)
    # plt.show()


streets = np.random.choice(sample_30k["starting_street"].unique(), 5)
plt.figure(figsize = (18.5, 10.5))
# for street in streets:
#     plt.boxplot(sample_30k.loc[sample_30k["starting_street"].isin([street]), ["travel_time_per_step"]].values)
plt.boxplot([[sample_30k.loc[sample_30k["starting_street"].isin([street]), ["travel_time_per_step"]].values] for street in streets])
names = streets
plt.xticks(range(1, len(names) +1), names)
plt.show()


plt.figure(figsize = (18.5, 10.5))
data = [[street,
    [sample_30k.loc[sample_30k["starting_street"].isin([street]), ["travel_time_per_step"]].values],
    sample_30k.loc[sample_30k["starting_street"].isin([street]), ["travel_time_per_step"]].median().values[0]]
    for street in streets]
plt.boxplot([street_data[0] for street_data in data])
[street_data[0] for street_data in data]
names = streets
data

plt.figure(figsize = (18.5, 10.5))
# x = np.column_stack([sample_30k.loc[sample_30k["starting_street"].isin([street]), ["travel_time_per_step"]] for street in streets])
