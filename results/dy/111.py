import json

# Specify the path to your JSON file
file_path = '01_crawler_title.txt'
# Read the JSON file line by line
with open(file_path, 'r') as file:
    for line in file:
        # Parse the JSON object from each line
        print(line.split(" ")[3][6:].strip())