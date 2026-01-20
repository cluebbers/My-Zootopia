import json


def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)


animals_data = load_data("animals_data.json")

output = ""
for animal in animals_data:
    output += '<li class="cards__item">\n'
    if "name" in animal:
        output += f'  <div class="card__title">{animal["name"]}</div>\n'
    output += '  <p class="card__text">\n'
    if "diet" in animal["characteristics"]:
        output += f'    <strong>Diet:</strong> {animal["characteristics"]["diet"]}<br/>\n'
    if "locations" in animal:
        output += f'    <strong>Location:</strong> {", ".join(animal["locations"])}<br/>\n'
    if "type" in animal["characteristics"]:
        output += f'    <strong>Type:</strong> {animal["characteristics"]["type"]}<br/>\n'
    output += "  </p>\n"
    output += "</li>\n"

print(output)

with open("animals_template.html", "r") as template_file:
    template = template_file.read()

template = template.replace("__REPLACE_ANIMALS_INFO__", output)

print(template)

with open("animals.html", "w") as output_file:
    output_file.write(template)
