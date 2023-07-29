# Specify the path to your file
file_path = '22.txt'

# Read the file line by line

with open(file_path, 'r') as file:

    for line in file:
        # Parse the JSON object from each line

        start_index = line.find("note_id': '") + len("note_id': '")
        end_index = line.find("', 'type':")
        content = line[start_index:end_index].strip()   
        print("https://www.xiaohongshu.com/explore/" + content)  
        #comments.append(content)  
#print(comments)
