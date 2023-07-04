import json

# Specify the path to your JSON file
file_path = '333.json'
database = []
note_id = []
database_notes = []
database_comments = []
# Read the JSON file line by line
with open(file_path, 'r') as file:
    for line in file:
        # Parse the JSON object from each line
        print(line.split(" ")[-1].strip())