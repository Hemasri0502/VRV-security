import csv

def save_log_data_to_csv(ip_counts, most_frequent_endpoint, suspicious_ips):
    try:
        # Open the CSV file in write mode
        with open('log_analysis_results.csv', mode='w', newline='') as file:
            writer = csv.writer(file)

            # Write the header row
            writer.writerow(["IP Address", "Request Count", "Endpoint", "Access Count", "Failed Login Attempts"])

            # Prepare data for writing into the file
            max_length = max(len(ip_counts), len(suspicious_ips))  # Find the max length of IP counts and suspicious IPs

            # Write the data
            for i in range(max_length):
                # Get IP request count data (IP Address, Request Count)
                ip_address, request_count = ip_counts[i] if i < len(ip_counts) else ("", "")
                
                # Get most frequent endpoint data (Endpoint, Access Count)
                endpoint, access_count = most_frequent_endpoint if i == 0 else ("", 0)
                
                # Get suspicious IP data (IP Address2, Failed Login Attempts)
                suspicious_ip, failed_attempts = suspicious_ips[i] if i < len(suspicious_ips) else ("", 0)

                # Write the row in CSV file
                writer.writerow([ip_address, request_count, endpoint, access_count,failed_attempts])

    except Exception as e:
        print(f"An error occurred while saving to CSV: {e}")
