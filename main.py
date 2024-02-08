import csv
import random

from random import randint
import json

# row = []
# with open("data.csv") as file:
#     data = csv.reader(file)
#     header = next(data)
#
#     for r in data:
#         row.append(r)
#
# print(row)

data = {
    "s_no": [],
    "shot_pressure": [],
    "melt_temp": [],
    "stroke_length": [],
    "die_temp": [],
    "cw_in_temp": [],
    "cw_out_temp": [],
    "cw_flow_rate": [],
    "cycle_time": [],
    "clamping_tonnage": [],
    "machine_vibration": []
}

for i in range(1,10001):
    data["s_no"].append(i)
    data["shot_pressure"].append(random.randrange(start=120, stop=149) + round(random.random(), 1))
    data["melt_temp"].append(random.randrange(start=650, stop=690) + round(random.random(), 1))
    data["stroke_length"].append(random.randrange(start=95, stop=107) + round(random.random(), 1))
    data["die_temp"].append(random.randrange(start=195, stop=225) + round(random.random(), 1))
    data["cw_in_temp"].append(random.randrange(start=15, stop=18) + round(random.random(), 1))
    data["cw_out_temp"].append(random.randrange(start=20, stop=23) + round(random.random(), 1))
    data["cw_flow_rate"].append(random.randrange(start=10, stop=13) + round(random.random(), 1))
    data["cycle_time"].append(random.randrange(start=130, stop=133) + round(random.random(), 1))
    data["clamping_tonnage"].append(random.randrange(start=98, stop=108) + round(random.random(), 1))
    data["machine_vibration"].append(random.randrange(start=32, stop=180) + round(random.random(), 1))

with open("test_data.json", "w") as file:
    json.dump(data, file)
