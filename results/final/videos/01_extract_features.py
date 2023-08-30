# Specify the path to your file
file_path = '01_crawler_title.txt'

# Read the file line by line

with open(file_path, 'r') as file:

    creator = {}

    for line in file:
        # Parse the JSON object from each line

        start_index = line.find("'nickname': '") + len("'nickname': '")
        end_index = line.find("', 'avatar':")
        content = line[start_index:end_index].strip()
        creator[content] = 1 
        
        #if content in creator:
        print (content)
        #print("https://www.xiaohongshu.com/explore/" + content)  
        #print(content)
        #comments.append(content) 
    #print(len(comments)) 
#print(comments)
