import json


def load_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


myJson = load_json('./warriors_2016_shots.json')
min = 300.0
for entry in myJson:
    if not entry["LOC_X"] and not entry["LOC_Y"]:
        print("Missing LOC_X and LOC_Y")
    elif entry["LOC_X"] == 0 and entry["SHOT_ZONE_BASIC"] == "Above the Break 3":
        print(abs(entry["LOC_Y"]) < min)
        if abs(entry["LOC_Y"]) < min:
            min = abs(entry["LOC_Y"])

print(min)
