# Specify the path to your file
file_path = '01_crawler_comments.txt'

# Read the file line by line
comments = []
note_id = []
data = {}

random = [53, 107, 2083, 2149, 2157, 2217, 2217, 2306, 2365, 2509, 2522, 2600, 2608, 2635, 2735, 2735, 2754, 2853, 3000, 3153, 3429, 3449, 3595, 3605, 3927, 4045, 4077, 4283, 4316, 4339, 4379, 4397, 4512, 4597, 4727, 4772, 4777, 4849, 4916, 5222, 5607, 5630, 5633, 5636, 5716, 5771, 5775, 5869, 5939, 5944, 6032, 6105, 6213, 6245, 6357, 6428, 6492, 6663, 6759, 6791, 6794, 6958, 7022, 7079, 7179, 7307, 7324, 7382, 7428, 7446, 7574, 7594, 7746, 7810, 8013, 8082, 8137, 8142, 8216, 8224, 8307, 8399, 8481, 8575, 8626, 8720, 8758, 8835, 8837, 9005, 9029, 9080, 9226, 9279, 9593, 9610, 9612, 9725, 9787, 9894, 9937, 9946, 10041, 10091, 10091, 10097, 10115, 10124, 10146, 10283, 10334, 10397, 10397, 10402, 10569, 10690, 10699, 10734, 10797, 10820, 10914, 10947, 11012, 11062, 11171, 11212, 11249, 11260, 11608, 11619, 11689, 11731, 11839, 11895, 12100, 12103, 12114, 12117, 12153, 12234, 12353, 12356, 12484, 12484, 12531, 12574, 12616, 12680, 12697, 12697, 12756, 12891, 12906, 12941, 13057, 13191, 13260, 13432, 13537, 13717, 13728, 13762, 13789, 13805, 13911, 13933, 13939, 13975, 14029, 14078, 14238, 14268, 14305, 14443, 14464, 14499, 14669, 14702, 14715, 14723, 14800, 14806, 15108, 15111, 15367, 15381, 15406, 15408, 15421, 15434, 15510, 15522, 15571, 15579, 15597, 15612, 15704, 15738, 15762, 15763, 15799, 15847, 15888, 15907, 15917, 15952]
sub_comments = 0
 
with open(file_path, 'r') as file:
    i = 1
    for line in file:
        # Parse the JSON object from each line
        if i in random:
            start_index = line.find("note_id': '") + len("note_id': '")
            end_index = line.find("', 'content': ")
            content = line[start_index:end_index].strip()   

            #print("https://www.xiaohongshu.com/explore/" + content)  
            comments.append(content)  
        i += 1
print(comments)