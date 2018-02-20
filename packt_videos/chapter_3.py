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

plt.rc("axes", prop_cycle = (cycler("color", palette_pastel)))
# pew = plt.rc("axes", prop_cycle = (cycler("color", palette_pastel)))
plt.rc()


cmap_dict = lambda : next(color_cycler)["color"]
cmap_dict()
palette
shuffle(palette)
palette
# palette2
# for i in palette:
#     print(i)
# plt.rcParams["axes.prop_cycle"]
plt.rc("axes", prop_cycle = (cycler("color", ["#54637a", "#54787a",
                                    "#547a63", "#6b7a54", "#918e5f",
                                    "#b29563", "#bf8765", "#bf7265",
                                    "#aa4747", "#824a53", "#824a6b",
                                    "#603f63", "#4e3f63"])))
#
# plt.rc('axes', prop_cycle=(cycler('color', ['r', 'g', 'b', 'y']) +
#                            cycler('linestyle', ['-', '--', ':', '-.'])))
# # color_cycler = cycle(plt.rcParams["axes.prop_cycle"])
# # cmap = lambda x: [x, next(color_cycler)["color"]]
# cmap = lambda: next(color_cycler)["color"]
# cmap()




total_exploded = pd.read_csv("~/quant/exploded.csv")


trip_ids = total_exploded["id"].unique()
sample_trips = np.random.choice(trip_ids, 500000)


sample_30k = total_exploded.loc[total_exploded["id"].isin(sample_trips), :]
# sample_30k.head()

sample_30k["starting_street"].unique().shape


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


streets = np.random.choice(sample_30k["starting_street"].unique(),5)
# plt.figure(figsize = (18.5, 10.5))
# # for street in streets:
# #     plt.boxplot(sample_30k.loc[sample_30k["starting_street"].isin([street]), ["travel_time_per_step"]].values)
# plt.boxplot([[sample_30k.loc[sample_30k["starting_street"].isin([street]), ["travel_time_per_step"]].values] for street in streets])
# names = streets
# plt.xticks(range(1, len(names) +1), names)
# plt.show()
#
#
# plt.figure(figsize = (23.5, 10.5))
#
# data = [[street,
#     [sample_30k.loc[sample_30k["starting_street"].isin([street]), ["travel_time_per_step"]].values],
#     sample_30k.loc[sample_30k["starting_street"].isin([street]), ["travel_time_per_step"]].median().values[0]]
#     for street in streets]
#
# data_sorted = sorted(data, key=lambda street: street[2])
#
# plt.boxplot([street_data[1] for street_data in data_sorted], 0, '', 0)
#
# names = [street_data[0] for street_data in data_sorted]
# plt.yticks(range(1, len(names) +1), names)
# plt.show()
#
# [street_data[2] for street_data in data_sorted]
#
# plt.figure(figsize = (18.5, 10.5))
# # x = np.column_stack([sample_30k.loc[sample_30k["starting_street"].isin([street]), ["travel_time_per_step"]] for street in streets])
#
# 5.is_integer()
# pew = 5.0





def plot_boxplots_groups(data_in, data_num, data_group, invert_axes = False,
                            order = "desc", order_by = "median",
                            show_outliers = True, get_top = False,
                            keycolor = "#232626",
                            # title = "Don't forget your titles.",
                            subtitle = "Don't forget your subtitles.",
                            xlabel = "Label X axis",
                            ylabel = "Label Y axis"):

    color_cycler = cycle(plt.rcParams["axes.prop_cycle"])
    # # cmap = lambda x: [x, next(color_cycler)["color"]]
    cmap = lambda: next(color_cycler)["color"]

    labels_to_filter = data_in.groupby([data_group]).size().sort_values(ascending = False).index
    if isinstance(int(get_top), int):
        group_labels = labels_to_filter[0:int(get_top)]

    if get_top == False:
        group_labels = labels_to_filter.tolist()

    if invert_axes == False:
        canvas_width = 0.4*len(group_labels)
        canvas_height = 13
    else:
        canvas_width = 13
        canvas_height = 0.4*len(group_labels)+ 0.8

    plt.figure(figsize = (canvas_width, canvas_height))
    if order_by == "mean":
        data = [[data_group_var,
            [data_in.loc[data_in[data_group].isin([data_group_var]), [data_num]].values],
            data_in.loc[data_in[data_group].isin([data_group_var]), [data_num]].mean().values[0]]
            for data_group_var in group_labels]

    elif order_by == "iqr":
        data = [[data_group_var,
            [data_in.loc[data_in[data_group].isin([data_group_var]), [data_num]].values],
            (data_in.loc[data_in[data_group].isin([data_group_var]), [data_num]].quantile(.75) - \
            data_in.loc[data_in[data_group].isin([data_group_var]), [data_num]].quantile(.25)).values[0]]
            for data_group_var in group_labels]

    elif order_by == "median":
        data = [[data_group_var,
            [data_in.loc[data_in[data_group].isin([data_group_var]), [data_num]].values],
            data_in.loc[data_in[data_group].isin([data_group_var]), [data_num]].median().values[0]]
            for data_group_var in group_labels]


    if order == "desc":
        data_sorted = sorted(data, key=lambda x: x[2])
    else:
        data_sorted = sorted(data, key=lambda x: x[2], reverse = True)

    if show_outliers:
        outlier_mark = "c"
    else:
        outlier_mark = ""

    if invert_axes:
        invert_value = 0
    else:
        invert_value = 1

    matplotlib.rc('axes', edgecolor=keycolor)
    # palette23 = ['#aa4747','#bf7265','#b29563','#54637a','#603f63','#824a53','#54787a',
    #             '#918e5f','#bf8765','#4e3f63','#824a6b','#547a63','#6b7a54']

    palette23 = ['#bcc19c','#c19c9e','#c19cbc','#c1a09c','#c19cac','#9c9dc1','#9cb0c1',
                '#c1b19c','#b29cc1','#9cc1bd','#9cc1a2']

    plt.rc("axes", prop_cycle = (cycler("color", palette23)))
    boxes = plt.boxplot([data_data[1] for data_data in data_sorted], 0, outlier_mark, invert_value,
                patch_artist = True,
                whiskerprops = {'color': "#9ea5a8", 'linewidth' : 9.5, 'zorder' : 0},
                medianprops = {'color': "#ffffff", 'linewidth' : 3, 'zorder' : 1000},
                # capprops = {'color': keycolor, 'linewidth' : 4},
                showcaps=False,

                boxprops = {'color': keycolor, 'facecolor': "#5e5757", 'zorder' : 999}
                # boxprops = {'color': keycolor, 'facecolor': keycolor, 'zorder' : 999}
                )
    cmap = lambda: next(color_cycler)["color"]
    # plot_cols = dict()
    for patch in boxes["boxes"]:
        patch.set_facecolor(cmap())
         # plot_cols[data_data[0]] = cmap(data_data[0])[1]
         # print(cmap())

    # print(pew["boxes"])

    names = [data_data[0] for data_data in data_sorted]
    # print(data_sorted)
    # print(names)
    if invert_axes:
        plt.yticks(range(1, len(names) +1), names, color=keycolor)
    else:
        plt.xticks(range(1, len(names) +1), names, color=keycolor)


    # Y axis label
    plt.ylabel(ylabel, color=keycolor,
               fontsize=12)
    # Y axis label
    plt.xlabel(xlabel, color=keycolor,
               fontsize=12)

    # Graph title
    # plt.suptitle(title,
    #             y=1.025, x = 0.12,
    #             # horizontalalignment="right",
    #             horizontalalignment="left",
    #             # horizontalalignment="center",
    #              fontsize=18, color=keycolor,
    #              )
    # plt.text(y=2, x = 0.12,
    #         s = subtitle, horizontalalignment = "left", fontsize=14, color=keycolor)

    # Graph subtitle
    plt.title(subtitle,
                y=1.01 , x = 0,
                 loc = "left", fontsize=18,
                color=keycolor)

    plt.savefig('/Users/ilyaperepelitsa/quant/pewpewpew231.jpg', dpi=300)
    plt.show()

plot_boxplots_groups(data_in = sample_30k, data_num = "travel_time_per_step",
                    data_group = "starting_street", invert_axes = True,
                    order = "desc", order_by = "iqr", show_outliers = False,
                    get_top = 10,
                    subtitle = "10 Most frequent Starting streets for 30k taxi trips. Time per maneuver.",
                    ylabel = "Trip starting street",
                    xlabel = "Travel time per maneuver")

plot_boxplots_groups(data_in = sample_30k, data_num = "travel_time_per_step",
                    data_group = "starting_street", invert_axes = True,
                    order = "desc", order_by = "mean", show_outliers = False,
                    get_top = 20)

plot_boxplots_groups(data_in = sample_30k, data_num = "travel_time_per_step",
                    data_group = "starting_street", invert_axes = True,
                    order = "desc", order_by = "iqr", show_outliers = False,
                    get_top = 30)

total_exploded.info()


##### DOTPLOT
sample_trips = np.random.choice(total_exploded["starting_street"].unique(), 3)
sample_1k = total_exploded.loc[total_exploded["starting_street"].isin(sample_trips), :]


sample_1k["starting_street"].unique().shape
sample_1k.shape



# sample_1k.head()
# plt.figure(figsize = (13, 5))
# one, two, three = [], [], []

color_cycler = cycle(plt.rcParams["axes.prop_cycle"])
# # cmap = lambda x: [x, next(color_cycler)["color"]]
cmap = lambda: next(color_cycler)["color"]
cmap = lambda x: next(color_cycler)["color"]
# plot_cols = dict()
# for patch in boxes["boxes"]:
#     patch.set_facecolor(cmap())


palette23 = ['#bcc19c','#c19c9e','#c19cbc','#c1a09c','#c19cac','#9c9dc1','#9cb0c1',
            '#c1b19c','#b29cc1','#9cc1bd','#9cc1a2']


palette = ['#aa4747','#bf7265','#b29563','#54637a','#603f63','#824a53','#54787a',
            '#918e5f','#bf8765','#4e3f63','#824a6b','#547a63','#6b7a54']

pew = []
cmap = lambda: next(color_cycler)["color"]
plt.figure(figsize = (10, 10))
plt.rc("axes", prop_cycle = (cycler("color", ["#547a63", "#4e3f63", "#aa4747"])))
plt.rcParams['axes.facecolor'] = '#252628'
for street in sample_1k["starting_street"].unique():

    plt.scatter(sample_1k.loc[sample_1k["starting_street"] == street, "lon"],
                sample_1k.loc[sample_1k["starting_street"] == street, "lat"],
                c = cmap(),alpha = 0.5, edgecolor = "none", linewidth = 0.5)

plt.axes().set_aspect("equal")
plt.show()

    # print(street)
