import csv
import re

def process_results():
    with open('result.log', 'r') as f:
        data = f.read()

    with open('test_results.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Test Case', 'Result'])
        for line in data.splitlines():
            if re.match(r'^\s*PASSED', line):
                writer.writerow(['Test Case', 'PASSED'])
            elif re.match(r'^\s*FAILED', line):
                writer.writerow(['Test Case', 'FAILED'])

if __name__ == "__main__":
    process_results()
