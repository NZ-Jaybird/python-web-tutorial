import json

sizes = ["S", "M", "L", "XL"]
colours = ["white", "brown", "grey", "black"]
garments = ["shirt", "hoodie", "trousers", "scarf"]

items = []

for size in sizes:
    for colour in colours:
        for garment in garments:
            items.append({"size": size, "colour": colour, "garment": garment})

with open("items.js", "w") as output_file:
    output_file.write("items = ")
    json.dump(items, output_file, indent=4)
