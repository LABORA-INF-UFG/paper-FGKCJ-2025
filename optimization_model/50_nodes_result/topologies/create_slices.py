import json
import sys

nDUs = int(sys.argv[1])
nNodes = int(sys.argv[2])

topologyJson = json.load(open("topology_{}_vDUs_{}_nodes/topology_{}_vDUs_{}_nodes.json".format(nDUs, nNodes, nDUs, nNodes)))

slices = []

for du in topologyJson["DUs"]:
    slices.append({
        "vDU": du["node"],
        "type": "URLLC",
        "max_delay": 1,
        "UE revenue": 0.118,
        "requirements": "(1024, 1024000)",
        "n_flows": 80
    })

    slices.append({
        "vDU": du["node"],
        "type": "eMBB",
        "requirement": "29201"
    })

json.dump({"slices": slices}, open("topology_{}_vDUs_{}_nodes/slices.json".format(nDUs, nNodes), "w"), indent=2)