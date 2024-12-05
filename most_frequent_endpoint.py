import re
import csv
from collections import Counter

def find_most_frequent_endpoint(file_path):
    try:
        with open(file_path, 'r') as log_file:
            log_data = log_file.readlines()

        endpoint_pattern = r'\"[A-Z]+\s+(/[^\s]*)'
        endpoints = []

        for line in log_data:
            match = re.search(endpoint_pattern, line)
            if match:
                endpoints.append(match.group(1))

        endpoint_counts = Counter(endpoints)

        most_frequent = endpoint_counts.most_common(1)

        return most_frequent[0] if most_frequent else ("None", 0)

    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return "None", 0
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return "None", 0


if __name__ == "__main__":
    log_file_path = r"C:\Users\kvhem\Downloads\HR-VRV\sample.log"

    print("\nProcessing log file...\n")

    endpoint, count = find_most_frequent_endpoint(log_file_path)

    print("Most Frequently Accessed Endpoint:")
    print(f"{endpoint} (Accessed {count} times)")
    

