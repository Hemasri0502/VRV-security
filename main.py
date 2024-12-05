from ip_address_request_count import parse_log_file
from most_frequent_endpoint import find_most_frequent_endpoint
from detect_suspicious_activity import detect_suspicious_activity
from save_to_csv import save_log_data_to_csv

if __name__ == "__main__":
    log_file_path = r"C:\Users\kvhem\Downloads\HR-VRV\sample.log"
    failed_attempt_threshold = 2  # Threshold for detecting suspicious activity

    print("\nProcessing log file...\n")

    # Process IP address request counts
    sorted_ip_counts = parse_log_file(log_file_path)
    if sorted_ip_counts:
        print("IP Address Request Counts:")
        for ip, count in sorted_ip_counts:
            print(f"{ip:<20} {count:<15}")

    # Find the most accessed endpoint
    endpoint, count = find_most_frequent_endpoint(log_file_path)
    print("\nMost Frequently Accessed Endpoint:")
    print(f"{endpoint} (Accessed {count} times)")

    # Detect suspicious activity
    suspicious_ips = detect_suspicious_activity(log_file_path, threshold=failed_attempt_threshold)
    if suspicious_ips:
        print("\nSuspicious Activity Detected:")
        for ip, count in suspicious_ips:
            print(f"{ip:<20} {count:<20}")
    else:
        print("\nNo suspicious activity detected.")

    # Save all data to CSV
    save_log_data_to_csv(sorted_ip_counts, (endpoint, count), suspicious_ips)
