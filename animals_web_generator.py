import json


def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)


animals_data = load_data("animals_data.json")

for animal in animals_data:
    output = []

    if "name" in animal:
        output.append(f"Name: {animal['name']}")

    if "characteristics" in animal:
        if "diet" in animal["characteristics"]:
            output.append(f"Diet: {animal['characteristics']['diet']}")
        if "type" in animal["characteristics"]:
            output.append(f"Type: {animal['characteristics']['type']}")

    if "locations" in animal:
        locations_str = ", ".join(animal["locations"])
        output.append(f"Location: {locations_str}")

    if output:
        print("\n".join(output) + "\n")
