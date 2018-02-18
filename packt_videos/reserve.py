
    plot_cols = dict()
    for data_data in data_sorted:
         # for data_data in data_sorted
         # print(data_data[0])
         # plot_cols[str(i)] = cmap(str(i))[1]
         plot_cols[data_data[0]] = cmap(data_data[0])[1]



color_cycler = cycle(plt.rcParams["axes.prop_cycle"])
cmap = lambda x: [x, next(color_cycler)["color"]]
