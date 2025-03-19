import json, pip

json_path = "control.json"
with open(json_path, encoding="UTF-8") as file:
    control = json.load(file)
    file_path = control["file_path"]
    frame_rate = control["frame_rate"]
    characters = control["characters"]

print(characters)
for i in range(0, 1%120, 1):
    print(i)
print(pip.__file__)