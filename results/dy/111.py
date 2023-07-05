# Specify the path to your file
file_path = '01_crawler_title.txt'

# Read the file line by line
with open(file_path, 'r') as file:
    for line in file:
        # Parse the object from each line
        #print("https://www.douyin.com/discover?modal_id=" + line.split(" ")[2][3:-1].strip())
        print(line.split(" ")[3].strip())