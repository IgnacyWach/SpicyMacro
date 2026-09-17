from pathlib import Path
import json

config_folder = Path("config")

config_folder.mkdir(exist_ok=True)

config_file = config_folder / "config.json"

if not config_file.exists():
    default_config = {
        "player_speed": "28",
        "hive_slot": "1",
        "webhook": "",
        "sendscreen": 0,
        "gathertime": "5 Minutes",
        "min_counter": "5 Minutes",
        "public_server": 1,
        "private_server_url": "",
        "field": "Dandelion Field",
        "where_field": "Center",
        "pattern": "Zigzag",
        "autorejoin": 1,
        "return_to_hive": 1
    }

    with open(config_file, "w") as file:
        json.dump(default_config, file, indent=4)

import json

def save(hive_slot, discord_webhookurl, player_speed, sendscreen, gathertime, min_counter, public, server, field, where_field, pattern, autore, return_to_hive):
    data = {
        "player_speed": player_speed,
        "hive_slot": hive_slot,
        "webhook": discord_webhookurl,
        "sendscreen": sendscreen,
        "gathertime": gathertime,
        "min_counter": min_counter,
        "public_server": public,
        "private_server_url": server,
        "field": field,
        "where_field": where_field,
        "pattern": pattern,
        "autorejoin": autore,
        "return_to_hive": return_to_hive
    }

    with open("config/config.json", "w") as file:
        json.dump(data, file, indent=4)


def load():
    with open("config/config.json", "r") as file:
        settings = json.load(file)
    return(settings)
