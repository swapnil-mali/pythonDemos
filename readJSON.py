#!/usr/bin/python3

import json

with open("sampleJSON.json", 'r') as file:
    jsonData = json.load(file)
    #print(type(jsonData))
    #print(jsonData)

print(jsonData['quiz'].keys())

for sub in jsonData['quiz'].keys():
    print("============= {} ============".format(sub))
    for que in jsonData['quiz'][sub]:
        print(jsonData['quiz'][sub][que]["question"])
        i = 1
        for option in jsonData['quiz'][sub][que]["options"]:
            print("{}. {}".format(i, option))
            i += 1
        print()

