import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np

x = [1, 2, 3]

# D-RAN
# y_DRAN = [21.034, 40, 40 - 21.034]
y_DRAN = [21.03, 100.23, 79.2]
y1 = y_DRAN

# C-RAN
# y_CRAN = [6.204, 11.5, 11.5 - 6.204]
y_CRAN = [6.2, 70.23, 64.02]
y2 = y_CRAN

# AllSplits
# y_AllSplits = [9.17, 40, 40 - 9.17]
y_AllSplits = [8.78, 92.14, 83.36]
y3 = y_AllSplits

# The data
# Calculate optimal width
width = np.min(np.diff(x)) / 4

fig = plt.figure(figsize=(8, 4))
ax = fig.add_subplot()
# matplotlib 3.0 you have to use align
ax.bar(x - width-width/2, y1, width, color='firebrick', label='-Ymin', align='edge', yerr=[0, 22.08, 22.08], capsize=3)
ax.bar(x-width/2, y2, width, color='royalblue', label='Ymax', align='edge', yerr=[0, 10.74, 10.74], capsize=3)
ax.bar(x + width-width/2, y3, width, color='navy', label='Ymax', align='edge', yerr=[1.08, 21.22, 22.09], capsize=3)

ax.yaxis.grid(color='gray', linestyle='--', linewidth=0.5)
# ax.set_yscale('log')
plt.rcParams.update({'font.size': 40})
plt.ylim(0, 125)

# f, ax = plt.subplots(figsize=(7, 3))

ax.tick_params(axis='y', which='major', labelsize=40)
ax.tick_params(axis='x', which='major', labelsize=40)

plt.xlim(0.5, 3.5)

plt.ylabel("Value (#)", fontsize=40)

plt.xticks([1, 2, 3])
plt.yticks([0, 40, 80, 120], fontsize=40)
ax.set_xticklabels(["Cost", "WAFC", "OF"])

# legend_elements = [Line2D([0], [0], color='firebrick', lw=3, label='D-RAN'),
#                    Line2D([0], [0], color='royalblue', lw=3, label='C-RAN'),
#                    Line2D([0], [0], color='navy', lw=3, label='NG-RAN Splits')]
# plt.legend(handles=legend_elements, loc="upper right", ncol=3)

plt.savefig("all_scenarios.pdf", bbox_inches='tight')

# plt.show()
