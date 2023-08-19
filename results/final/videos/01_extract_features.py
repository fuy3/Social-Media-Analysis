# Specify the path to your file
file_path = '01_crawler_title.txt'

# Read the file line by line

with open(file_path, 'r') as file:

    for line in file:
        # Parse the JSON object from each line

        start_index = line.find("'liked_count': '") + len("'liked_count': '")
        end_index = line.find("', 'collected_count':")
        content = line[start_index:end_index].strip()   
        
        #print("https://www.xiaohongshu.com/explore/" + content)  
        print(content)
        #comments.append(content)  
#print(comments)
