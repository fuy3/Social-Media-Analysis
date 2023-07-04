# Specify the path to your input file
file_path = '111.txt'
# Read the JSON file line by line
dic = {}
with open(file_path, 'r') as file:
    for line in file:
        # Parse the JSON object from each line

        word = line.split(",")[0]
        counts = line.split(",")[-1].strip()
        if counts != "":
            dic[word] = counts
# Sort the dictionary items by values in descending order
sorted_items = sorted(dic.items(), key=lambda x: int(x[1]), reverse=True)

# Print the sorted items
for item in sorted_items:
    word, counts = item
    print(word + "," + counts)
