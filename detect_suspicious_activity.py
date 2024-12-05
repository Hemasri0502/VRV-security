import re
from collections import Counter

def detect_suspicious_activity(file_path, threshold=10):

    try:
        with open(file_path, 'r') as log_file:
            log_data = log_file.readlines()

        ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
        failed_login_pattern = r'HTTP/1\.1"\s401.*"Invalid credentials"'


        failed_attempts = []

        # Extract failed login attempts and their corresponding IP addresses
        for line in log_data:
            if re.search(failed_login_pattern, line):
                match = re.search(ip_pattern, line)
                if match:
                    failed_attempts.append(match.group())

        # Count occurrences of failed attempts per IP
        failed_attempt_counts = Counter(failed_attempts)

        # Filter IPs exceeding the threshold
        suspicious_ips = [(ip, count) for ip, count in failed_attempt_counts.items() if count > threshold]

        # Sort the results in descending order of failed login attempts
        suspicious_ips.sort(key=lambda x: x[1], reverse=True)

        return suspicious_ips

    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

def display_suspicious_activity(suspicious_ips):
    
    if suspicious_ips:
        print("\nSuspicious Activity Detected:")
        print(f"{'IP Address':<20} {'Failed Login Attempts':<20}")
        print("-" * 40)
        for ip, count in suspicious_ips:
            print(f"{ip:<20} {count:<20}")
    else:
        print("\nNo suspicious activity detected.")

if __name__ == "__main__":
    log_file_path = r"C:\Users\kvhem\Downloads\HR-VRV\sample.log"
    failed_attempt_threshold = 2  # Default threshold for flagging suspicious activity

    print("\nAnalyzing log file for suspicious activity...\n")

    suspicious_ips = detect_suspicious_activity(log_file_path, threshold=failed_attempt_threshold)

    display_suspicious_activity(suspicious_ips)
