import json
from datetime import datetime


def save_to_json(data):
    now = datetime.now()

    # Create filename
    city = data.get("City", "unknown").lower().replace(" ", "_")
    date_time = now.strftime("%d%m%Y_%H%M%S")

    filename = f"{city}_{date_time}.json"

    # Save data to file
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
