import os
import json
from os.path import isfile, join

THEMES_PATH = "/home/monosen/.config/qtile/themes"
CONFIG_PATH = "/home/monosen/.config/qtile/config.json"

with open(CONFIG_PATH, "r", encoding="utf-8") as config_file:
    config = json.load(config_file)

# Obtener una lista de los temas existentes
themes = [name for name in os.listdir(THEMES_PATH) if isfile(join(THEMES_PATH, name)) and name.endswith(".json")]
print(themes)
# Obtener el índice del tema actual
current_theme = f"{config['theme']}.json"
if current_theme in themes:
    current_theme_index = themes.index(current_theme)
else:
    current_theme_index = -1

# Establecer el tema siguiente
if themes:
    next_theme_index = (current_theme_index + 1) % len(themes)
    config["theme"] = themes[next_theme_index].replace(".json", "")

with open(CONFIG_PATH, "w", encoding="utf-8") as config_file:
    json.dump(config, config_file, ensure_ascii=False)
