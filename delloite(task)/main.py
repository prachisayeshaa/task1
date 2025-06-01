import json
from datetime import datetime

def iso_to_millis(iso_str):
    """Convert ISO 8601 timestamp to milliseconds since epoch"""
    dt = datetime.strptime(iso_str, "%Y-%m-%dT%H:%M:%S.%fZ")
    return int(dt.timestamp() * 1000)

def convert_data1(data1):
    """Convert data from data-1.json format to unified format"""
    result = []
    for entry in data1:
        converted_entry = {
            "device_id": entry["device_id"],
            "timestamp": iso_to_millis(entry["timestamp"]),
            "value": entry["value"]
        }
        result.append(converted_entry)
    return result

def convert_data2(data2):
    """Convert data from data-2.json format to unified format"""
    result = []
    for entry in data2:
        converted_entry = {
            "device_id": entry["device"],
            "timestamp": entry["time"],
            "value": entry["reading"]
        }
        result.append(converted_entry)
    return result

def main():
    # Load data from data-1.json
    with open("data-1.json", "r") as f1:
        data1 = json.load(f1)

    # Load data from data-2.json
    with open("data-2.json", "r") as f2:
        data2 = json.load(f2)

    # Convert both datasets
    unified_data = convert_data1(data1) + convert_data2(data2)

    # Sort the data by timestamp (optional but useful)
    unified_data.sort(key=lambda x: x["timestamp"])

    # Save to data-result.json
    with open("data-result.json", "w") as fout:
        json.dump(unified_data, fout, indent=2)

    print("Conversion complete. Output saved to data-result.json")

if __name__ == "__main__":
    main()