#!/usr/bin/python3

import json


dict1 = {
            "student_Data":
            {
                "name": "Adam",
                "rollno": 1,
                "presense": True,
                "sports": None
            }
        }

with open("studentData.JSON", 'w') as file:
    json.dump(dict1, file)

