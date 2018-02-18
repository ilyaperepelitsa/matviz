
plot_cols = dict()
for data_data in data_sorted:
     plot_cols[data_data[0]] = cmap(data_data[0])[1]



color_cycler = cycle(plt.rcParams["axes.prop_cycle"])
cmap = lambda x: [x, next(color_cycler)["color"]]
