import json

for i in range(1, 257):

    json_obj = json.load(open("4_vDUs_3_nodes_random_{}/slices.json".format(i)))

    for s in json_obj["slices"]:
        if s["type"] == "URLLC" and s["max_delay"] == 0.001:
            new_s = s.copy()
            new_s["max_delay"] = 0.01
            json_obj["slices"].append(new_s)
            json.dump(json_obj, open("4_vDUs_3_nodes_random_{}/slices.json".format(i), 'w'))