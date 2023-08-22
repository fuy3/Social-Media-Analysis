# Specify the path to your file
file_path = 'notes_20_all_comments.txt'

# Read the file line by line

with open(file_path, 'r') as file:

    comments = {}

    for line in file:
        # Parse the JSON object from each line

        start_index = line.find("'note_id': '") + len("'note_id': '")
        end_index = line.find("', 'type': ")
        content = line[start_index:end_index].strip()   
        
        if content in comments:
            print (content)
        comments[content] = 1
        #print("https://www.xiaohongshu.com/explore/" + content)  
        #print(content)
        #comments.append(content) 
    print(len(comments)) 
#print(comments)
