import re
from collections import Counter

def parse_log_file(file_path):
    try:
        with open(file_path, 'r') as log_file:
            log_data = log_file.readlines()
        
        # Regex pattern to extract IP addresses
        ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
        ip_addresses = []

        # Extract IP addresses from each line of the log
        for line in log_data:
            match = re.search(ip_pattern, line)
            if match:
                ip_addresses.append(match.group())

        # Count occurrences of each IP
        ip_counts = Counter(ip_addresses)

        # Sort IPs by request count in descending order
        sorted_ip_counts = sorted(ip_counts.items(), key=lambda x: x[1], reverse=True)

        return sorted_ip_counts

    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

def display_results(sorted_ip_counts):

    print(f"{'IP Address':<20} {'Request Count':<15}")
    print("-" * 35)
    for ip, count in sorted_ip_counts:
        print(f"{ip:<20} {count:<15}")

