"""
    This script calulates the newest corona data
"""
import json
from s3_utils import upload_to_s3
from corona_api_service import fetch_corona_data

def determine_corona_status(corona_data_input):
    """
        determine the status of corona data from input
    """
    latest_item = corona_data_input[-1]
    active = corona_data_input[-1]["Cases"] - corona_data_input[-14]["Cases"]
    active_before_seve_days = corona_data_input[-7]["Cases"] - corona_data_input[-21]["Cases"]
    trend = "UP" if active > active_before_seve_days else "DOWN"
    lockdown = corona_data_input[-1]["Cases"] - corona_data_input[-7]["Cases"] > 10000
    return {
        "cases": latest_item["Cases"],
        "active": active,
        "trend": trend,
        "lockdown": lockdown
    }


def save_status(status, filename):
    """
       save status to file
    """
    with open(filename, "w", encoding= "UTF-8") as file:
        json.dump(status, file)


corona_data = fetch_corona_data()
corona_status = determine_corona_status(corona_data)
save_status(corona_status, "corona-data.json")
upload_to_s3("corona-data.json")
print(corona_status)
