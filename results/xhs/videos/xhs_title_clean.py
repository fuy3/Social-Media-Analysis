# Specify the path to your file
file_path = '01_crawler_title.txt'

# Read the file line by line
comments = {}
with open(file_path, 'r') as file:
    for line in file:
        # Parse the JSON object from each line
        aa = "https://www.xiaohongshu.com/explore/" + line.split(" ")[3][1:-2]
        bb = line.split(" ")
        cc = [bb[7][1:-2],bb[9][1:-2]]

        i = 0
        while i < len(bb):
            if bb[i] == "'nickname':":
                cc.append(bb[i+1][1:-2])
                cc.append("https://www.xiaohongshu.com/user/profile/" + bb[i-1][1:-2])
            i += 1
        comments[aa] = cc

user_dic = {}
users = ['博乐-乐爸', '🌈琦琦宝贝', '恩启', '自闭症轩轩', 'MySt', 'ALSOLIFE', '废柴妈妈日记', '四川观察', '安安大忙人', '阳光舒海峰的钢琴世界', '闪送', '江寻千', '萱妈与萱宝', '哈哈哈士奇', '高大福', '星儿守望者', '小完追剧', '北医脑健康', '唐唐', '我的大诗姐啊', '九九妈妈', '报姐唠唠', '泡泡尤剧社', '爆米花', '安善星语特殊教育', 'Ta天使（精神抚慰犬基地）', '温暖电影', '宝藏兔姐', '落日向童', '路人甲电影', '夏天讲电影', '萌芽熊Doorobear', '一语道破', '可乐麻麻育儿感统公益分享', '蜗宝妈咪🐌', '融合星教育', '北极圈芬兰大鱼', '小东北侃大片', '特教张文静', '睡觉瓜', '安安妈妈francie', '澳洲中文教育学院Jo校长', '七喃喃']
for i in comments:
    #print(i)
    if comments[i][-2] in users:
        user_dic[comments[i][-2]] = comments[i][-1]
for i in users:
    print(user_dic[i])