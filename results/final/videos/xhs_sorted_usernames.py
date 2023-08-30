from collections import Counter

aa = []
bb = []
def print_username_counts(text):
    usernames = text.splitlines()
    username_counts = Counter(usernames)

    sorted_counts = sorted(username_counts.items(), key=lambda x: x[1], reverse=True)
        
    for username, count in sorted_counts:
        aa.append(username)
        print(username)
        #print(count)

# 读取文件内容
filename = '111.txt'
with open(filename, 'r') as file:
    file_content = file.read()

# 打印用户名及出现次数
print_username_counts(file_content)
#print(aa)
