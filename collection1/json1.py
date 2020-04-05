import json
import demjson


# Key:value mapping
student = {
    "Name": "Peter",
    "Roll_no": "0090014",
    "Grade": "A",
    "Age": 20,
    "Subject": ["Computer Graphics", "Discrete Mathematics", "Data Structure"]
}

with open("data.json", "w") as write_file:
    json.dump(student, write_file)

with open("data.json", "r") as read_file:
    b = json.load(read_file)
print(b)
print(json.dumps(b, indent=5, sort_keys=True))
print(demjson.decode(b))