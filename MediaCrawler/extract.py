import json

# Specify the path to your JSON file
file_path = 'ASD2.json'
database = []
note_id = []
database_notes = []
database_comments = []
# Read the JSON file line by line
with open(file_path, 'r') as file:
    for line in file:
        # Parse the JSON object from each line
        database.append(line.split(","))
        header = line.split(",")[0]
        if header.split(" ")[2] == "comment:":
            database_comments.append(header.split(" ")[2:])
        else:
            database_notes.append(header.split(" ")[2:])
    print(database_notes[0])
    
    for i in database_notes:
        print(i)
