# Python script to calculate average throughput from iperf3 output

import re

# Replace with your actual file name
filename = 'iperf_output.txt'

# List to store extracted throughput values
throughputs = []

# Open and read the file
with open(filename, 'r') as file:
    for line in file:
        # Match lines with interval and Mbits/sec
        match = re.search(r'\d+\.\d+-\d+\.\d+\s+sec\s+[\d\.]+\s+MBytes\s+([\d\.]+)\s+Mbits/sec', line)
        if match:
            throughput = float(match.group(1))
            print(f"Found throughput {throughput}")
            throughputs.append(throughput)

# Remove final summary lines if needed (optional)
# You can add a filter if necessary

# Calculate average
if throughputs:
    avg_throughput = sum(throughputs) / len(throughputs)
    print(f"Average Throughput: {avg_throughput:.2f} Mbits/sec")
else:
    print("No throughput data found!")
