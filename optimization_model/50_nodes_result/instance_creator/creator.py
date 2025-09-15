import os
import json
import copy
import random

numbers = [80, 60, 40, 20]
eMBB_demand = {80: 29201, 60: 58243, 40: 87109, 20: 117810}
vDUs = [5, 6, 9, 10]
random.seed(5)
scenarios = []

for n1 in numbers:
    for n2 in numbers:
        for n3 in numbers:
            for n4 in numbers:
                # if len(scenarios) < 50:
                #     if not n1 == n2 == n3 == n4 or random.randint(0, 3) == 1:
                scenarios.append([n1, n2, n3, n4])

print(len(scenarios))

scenarios_count = 1

for demand in scenarios:
    json_dict = {"slices": []}
    index = 0
    for d in demand:
        json_dict["slices"].append({"vDU": vDUs[index], "type": "URLLC", "max_delay": 0.001, "bw_slice": 1, "UE revenue": 0.118, "requirements": "(1024, 1024000)", "n_flows": d})
        json_dict["slices"].append({"vDU": vDUs[index], "type": "eMBB", "requirement": str(eMBB_demand[d])})
        index += 1
    print(json_dict)

    os.system("mkdir ../topologies/evaluation_topologies/4_vDUs_3_nodes_random_{}".format(scenarios_count))
    os.system("cp ../topologies/evaluation_topologies/4_vDUs_3_nodes_random_1/paths.json ../topologies/evaluation_topologies/4_vDUs_3_nodes_random_{}".format(scenarios_count))
    os.system("cp ../topologies/evaluation_topologies/4_vDUs_3_nodes_random_1/topology_4_vDUs_3_nodes.json ../topologies/evaluation_topologies/4_vDUs_3_nodes_random_{}".format(scenarios_count))
    json.dump(json_dict, open("../topologies/evaluation_topologies/4_vDUs_3_nodes_random_{}/slices.json".format(scenarios_count), 'w'))
    scenarios_count += 1