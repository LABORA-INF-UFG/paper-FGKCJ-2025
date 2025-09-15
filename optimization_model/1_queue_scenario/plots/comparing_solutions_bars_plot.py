import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np

x = [1, 2, 3]

# D-RAN
# y_DRAN = [21.034, 40, 40 - 21.034]
y_DRAN = [21.03, 25.06, 4.02]
y1 = y_DRAN

# C-RAN
# y_CRAN = [6.204, 11.5, 11.5 - 6.204]
y_CRAN = [6.2, 19.08, 12.88]
y2 = y_CRAN

# AllSplits
# y_AllSplits = [9.17, 40, 40 - 9.17]
y_AllSplits = [7.96, 24.9, 16.95]
y3 = y_AllSplits

# The data
# Calculate optimal width
width = np.min(np.diff(x)) / 4

fig = plt.figure(figsize=(8, 4))
ax = fig.add_subplot()
# matplotlib 3.0 you have to use align
ax.bar(x - width-width/2, y1, width, color='firebrick', label='-Ymin', align='edge', yerr=[0, 5.52, 5.52], capsize=3)
ax.bar(x-width/2, y2, width, color='royalblue', label='Ymax', align='edge', yerr=[0, 1.87, 1.87], capsize=3)
ax.bar(x + width-width/2, y3, width, color='navy', label='Ymax', align='edge', yerr=[0.9, 4.66, 5.52], capsize=3)

ax.yaxis.grid(color='gray', linestyle='--', linewidth=0.5)
# ax.set_yscale('log')
plt.rcParams.update({'font.size': 40})
# plt.ylim(0, 31)

# f, ax = plt.subplots(figsize=(7, 3))

ax.tick_params(axis='y', which='major', labelsize=40)
ax.tick_params(axis='x', which='major', labelsize=40)

plt.xlim(0.5, 3.5)

plt.ylabel("Value (#)", fontsize=40)

plt.xticks([1, 2, 3])
plt.yticks([0, 10, 20, 30], fontsize=40)
ax.set_xticklabels(["Cost", "WAFC", "OF"])

# legend_elements = [Line2D([0], [0], color='firebrick', lw=3, label='D-RAN'),
#                    Line2D([0], [0], color='royalblue', lw=3, label='C-RAN'),
#                    Line2D([0], [0], color='navy', lw=3, label='NG-RAN Splits')]
# plt.legend(handles=legend_elements, loc="upper right", ncol=3)

plt.savefig("all_scenarios.pdf", bbox_inches='tight')

# plt.show()
