import json
import matplotlib.pyplot as plt

fontsize = 16
markersize = 10
linewidth = 2.5
linestyle = '--'

nNodes = [10, 20, 30, 40, 50, 60]
DUs = [4, 6, 8, 10, 12, 14]

OFAllSplits = []
OFOnlyCRAN = []
OFOnlyDRAN = []

WAFCAllSplits = []
WAFCOnlyCRAN = []
WAFCOnlyDRAN = []

CostAllSplits = []
CostOnlyCRAN = []
CostOnlyDRAN = []

for n in DUs:
    jsonFile = json.load(open("../optimization_model/new_plot_results/All_splits/{}.json".format(n)))
    solution = jsonFile["solution"]
    OFAllSplits.append(solution["efficiency"])
    WAFCAllSplits.append(solution["revenue"])
    CostAllSplits.append(solution["cost"])

    jsonFile = json.load(open("../optimization_model/new_plot_results/Only_C-RAN/{}.json".format(n)))
    solution = jsonFile["solution"]
    OFOnlyCRAN.append(solution["efficiency"])
    WAFCOnlyCRAN.append(solution["revenue"])
    CostOnlyCRAN.append(solution["cost"])

    jsonFile = json.load(open("../optimization_model/new_plot_results/Only_D-RAN/{}.json".format(n)))
    solution = jsonFile["solution"]
    OFOnlyDRAN.append(solution["efficiency"])
    WAFCOnlyDRAN.append(solution["revenue"])
    CostOnlyDRAN.append(solution["cost"])

plt.figure(figsize=(10, 4))
plt.plot(nNodes, OFOnlyCRAN, color="royalblue", marker='o', label='Split O9', markersize=markersize, linestyle=linestyle, linewidth=linewidth)
plt.plot(nNodes, OFOnlyDRAN, color="firebrick", marker='o', label='Split O1', markersize=markersize, linestyle=linestyle, linewidth=linewidth)
plt.plot(nNodes, OFAllSplits, color="navy", marker='o', label='FFS', markersize=markersize, linestyle=linestyle, linewidth=linewidth)
plt.ylabel('OF (#)', fontsize=fontsize)
plt.xlabel('Number of Nodes (#)', fontsize=fontsize)
plt.legend(fontsize=fontsize, ncol=3)
plt.grid(True, linewidth=0.5, linestyle='--')
plt.xticks(nNodes, fontsize=fontsize)
plt.yticks(fontsize=fontsize)
plt.tight_layout()
plt.savefig('OF.pdf', dpi=300, bbox_inches='tight')
