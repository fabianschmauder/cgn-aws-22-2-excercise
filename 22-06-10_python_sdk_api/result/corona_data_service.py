import json
from s3_utils import upload_to_s3
from corona_api_service import fetch_corona_data

def determine_corona_status(corona_data):
    latest_item = corona_data[-1]
    active = corona_data[-1]["Cases"] - corona_data[-14]["Cases"]
    active_before_seve_days = corona_data[-7]["Cases"] - \
        corona_data[-21]["Cases"]
    trend = "UP" if active > active_before_seve_days else "DOWN"
    lockdown = corona_data[-1]["Cases"] - corona_data[-7]["Cases"] > 10000
    return {
        "cases": latest_item["Cases"],
        "active": active,
        "trend": trend,
        "lockdown": lockdown
    }


def save_status(status, filename):
    with open(filename, "w") as file:
        json.dump(status, file)


corona_data = fetch_corona_data()
corona_status = determine_corona_status(corona_data)
save_status(corona_status, "corona-data.json")
upload_to_s3("corona-data.json")
print(corona_status)
