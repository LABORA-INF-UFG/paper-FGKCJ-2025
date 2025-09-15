import json
import networkx as nx
import sys
import os

q_vDUs = sys.argv[1]
q_nodes = sys.argv[2]
# topology_obj = json.load(open("evaluation_topologies/{}_vDUs_{}_nodes_{}/topology_{}_vDUs_{}_nodes.json".format(q_vDUs, q_nodes, sys.argv[3], q_vDUs, q_nodes)))
topology_obj = json.load(open("topology_{}_vDUs_{}_nodes/topology_{}_vDUs_{}_nodes.json".format(q_vDUs, q_nodes, q_vDUs, q_nodes)))

nodes = topology_obj["nodes"]
DUs = topology_obj["DUs"]
links = topology_obj["links"]

nodes_ID_list = []
DUs_node_ID_list = []
links_tuple_list = []
links_delay = {}

for node in nodes:
    nodes_ID_list.append(node["ID"])

for DU in DUs:
    DUs_node_ID_list.append(DU["node"])

for link in links:
    links_tuple_list.append((link["from_Node"], link["to_Node"]))
    links_tuple_list.append((link["to_Node"], link["from_Node"]))
    links_delay[(link["from_Node"], link["to_Node"])] = link["delay"]
    links_delay[(link["to_Node"], link["from_Node"])] = link["delay"]

nodes_without_DU = []

for n in nodes_ID_list:
    if n not in DUs_node_ID_list and n not in [0, 1]:
        nodes_without_DU.append(n)

G = nx.Graph()
G.add_nodes_from(nodes_ID_list)
G.add_edges_from(links_tuple_list)

paths = {}
id = 0

for du in DUs_node_ID_list:
    X = nx.shortest_simple_paths(G, 0, du)
    k = 3
    for counter, path in enumerate(X):
        print(path)
        paths["path-{}".format(id)] = {"source": path[0],
                                       "target": path[len(path)-1],
                                       "seq": path,
                                       "delay": [links_delay[(path[i], path[i+1])] for i in range(0, len(path)-1)]}
        id += 1
        if counter == k - 1:
            break

json.dump(paths, open("topology_{}_vDUs_{}_nodes/paths.json".format(q_vDUs, q_nodes), 'w'), indent=2)