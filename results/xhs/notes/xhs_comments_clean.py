# Specify the path to your file
file_path = '01_crawler_comments.txt'

# Read the file line by line
comments = []
with open(file_path, 'r') as file:
    for line in file:
        # Parse the JSON object from each line
        aa = line.split(" ")
        i = 0
        while i < len(aa):
            if aa[i] == "'content':":
                comments.append(aa[i+1][1:-2])
                print(aa[i+1][1:-2])
            i += 1