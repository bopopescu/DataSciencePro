import requests
import json

x = requests.get('https://api.github.com/users/cmpundhir')
print(x.text)
with open("data2.json", "w") as write_file:
     json.dump(x.text,write_file)

with open('data2.json', 'r') as f:
    distros_dict = json.load(f)
s=str(distros_dict)
print(type(s))
json_acceptable_string = s.replace("'", "\"")
d = json.loads(json_acceptable_string)
print("Image url: " ,d["avatar_url"])

