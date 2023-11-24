import csv
import random

# Generate 1000 random uniform float numbers between 0 and 1
random_numbers = [random.uniform(0, 1.01) for _ in range(6000)]
random_numbers2 = [random.uniform(0, 1.01) for _ in range(6000)]

# Specify the header for the CSV file
header = ['cpu_usage', 'memory_usage']

# Combine header and random numbers into a list of dictionaries
data = [{'cpu_usage': f'{value:.4f}', 'memory_usage': f'{value2:.4f}'} for value, value2 in zip(random_numbers, random_numbers2)]

# Specify the CSV file name
csv_file_name = 'random_cpu_usage6.csv'

# Write the data to the CSV file
with open(csv_file_name, 'w', newline='') as csv_file:
    # Create a CSV writer object
    csv_writer = csv.DictWriter(csv_file, fieldnames=header)

    # Write the header to the CSV file
    csv_writer.writeheader()

    # Write the data to the CSV file
    csv_writer.writerows(data)

print(f"Random CPU usage data between 0 and 1 has been written to '{csv_file_name}'.")
