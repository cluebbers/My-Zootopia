import json


def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)


animals_data = load_data("animals_data.json")

output = ""
for animal in animals_data:
    if "name" in animal:
        output += f"Name: {animal['name']}\n"
    if "diet" in animal["characteristics"]:
        output += f"Diet: {animal['characteristics']['diet']}\n"
    if "locations" in animal:
        output += f"Location: {', '.join(animal['locations'])}\n\n"
    if "type" in animal["characteristics"]:
        output += f"Type: {animal['characteristics']['type']}\n"

print(output)

with open("animals_template.html", "r") as template_file:
    template = template_file.read()

template = template.replace("__REPLACE_ANIMALS_INFO__", output)

print(template)

with open("animals.html", "w") as output_file:
    output_file.write(template)
