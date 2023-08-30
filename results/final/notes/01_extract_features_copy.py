import pandas as pd
import os
# Specify the path to your file
file_path = '01_crawler_comments.txt'

# Read the file line by line

with open(file_path, 'r') as file:

    contents = {}

    for line in file:
        # Parse the JSON object from each line

        start_index = line.find("'note_id': '") + len("'note_id': '")
        end_index = line.find("', 'content':")
        content = line[start_index:end_index].strip()

        #contents[content] = comments

        start_index1 = line.find("'content': '") + len("'content': '")
        end_index1 = line.find("', 'user_id': ")
        #comments = [line[start_index1:end_index1].strip()]

        start_index2 = line.find("omment_count': ") + len("omment_count': ")
        end_index2 = line.find(", 'last_modi")

        sub = line[start_index2:end_index2].strip()

        if sub != 'None' and sub != "'0'":
            print(sub.strip("'"))

        comment = [line[start_index1:end_index1].strip(), line[start_index2:end_index2].strip()]

        if content in contents:
            contents[content].append([line[start_index1:end_index1].strip(), line[start_index2:end_index2].strip()])
        else:
            contents[content] = [comment]
        
        #if content in creator:
        #print (content)
        #print("https://www.xiaohongshu.com/explore/" + content)  
        #print(content)
        #comments.append(content) 
    #print(len(comments)) 

"""
output_folder = 'video_comments'
os.makedirs(output_folder, exist_ok=True)

file_path2 = '222.txt'
rank = 1

with open(file_path2, 'r') as file:
    for line in file:
        if line.strip() in contents:
            line_data = contents[line.strip()]
        else:
            line_data = ["There're no comments under this post"]
        filename = os.path.join(output_folder, str(rank) + '.xlsx')
        
        # 创建一个DataFrame
        df = pd.DataFrame(line_data)
        
        # 将DataFrame保存为Excel文件
        df.to_excel(filename, index=False)
        
        rank += 1
    """