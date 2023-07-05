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
users = ['枣红色', '金鱼黄LunaSue', '君子若兰', '言语训练吴老师', 'ALSOLIFE', '又龙又虾', '', '一只深海的鲸鱼🐳', 'Sail', '蜗牛快跑', 'ABA行为治疗', '咚巴拉飒飒の影单', '阳光舒海峰的钢琴世界', '池小羊', '三胞胎小可爱', '荒坂西八', '乔治兄弟', '周哼哼', '奔跑吧兄弟', '安安妈妈francie', '快乐发芽', 'stellina_💫', '艾林Lin', 'Double鱼🐠', '🌈琦琦宝贝', '52hz', 'Ciara_', 'Jerry炒鸡可爱滴🌸', '看我成长儿童行为指导中心', '栽个月亮', '我的Naomi爱画画', '冯绮虾', '汉堡妈妈说自闭', '张若伊', '黄辣丁💓', '全职陪读的孩子他爸', '爱喝酸奶', '鱼丸爱推文', '喵喵酱', '水水水设计💦', '梅梅', '七九吖', '小鱼说自闭症', '颜小溪', '自闭症孩子田田的世界', '武汉北斗星儿童小助手', '王老师家在外地', '尼尼和鹿鹿', '武汉乐可自闭症康复教育', 'CC爱看小说', '脸脸仔', '四颗牙小花老师', '乌冬面加盐', '西西吖', 'Patricia爱Hua的小小仙女', '来自星星的你', '萌娃之家儿童康复咨询', '惘小政', '狗蛋', '南宁市护苗教育中心', '小猪🐷', '龍角散', '胡加灵', '树叶', '拓慧智元教育咨询', '温妞妞', '阿冬', '特殊儿童资料站', '杨婷是特教老师啊', '小弗的村庄', '红米粒急救', '星力量展能', '快乐QQ千夏', '艺术系胞', '丢丢产品设计师', '永安一定好起来啊', 'Roxy', 'YH妈妈', '该吃水果了', '育婴师包子欣', 'IN', 'Spice教育设计', '言语坊', '杭州自闭症、发育迟缓康复']

for i in comments:
    print(comments[i][2])
    """"
    if comments[i][-2] in users:
        user_dic[comments[i][-2]] = comments[i][-1]
for i in users:
    print(i)
    """