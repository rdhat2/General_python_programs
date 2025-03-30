import re
from collections import defaultdict

def count_status_codes(log_file):
    """
    Counts the occurrences of each HTTP status code in the log file.
    
    :param log_file: Path to the web server log file.
    """
    status_code_pattern = re.compile(r'"\s(\d{3})\s')
    status_counts = defaultdict(int)
    
    with open(log_file, 'r') as infile:
        for line in infile:
            match = status_code_pattern.search(line)
            if match:
                status_code = match.group(1)
                status_counts[status_code] += 1
    
    print("Status Code Counts:")
    for status_code, count in status_counts.items():
        print(f"{status_code}: {count}")

# Usage
if __name__ == "__main__":
    count_status_codes('access.log')
