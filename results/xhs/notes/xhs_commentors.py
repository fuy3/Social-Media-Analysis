# Specify the path to your file
file_path = '01_crawler_comments.txt'

# Read the file line by line
comments = {}
with open(file_path, 'r') as file:
    for line in file:
        # Parse the JSON object from each line
        start_index = line.find("'nickname': '") + len("'nickname': '")
        end_index = line.find("', 'avat")
        content = line[start_index:end_index].strip()

        start_index2 = line.find("'user_id': '") + len("'user_id': '")
        end_index2 = line.find("', 'nicknam")
        link = line[start_index2:end_index2].strip()    

        comments[content] = link

user_dic = {}
users = ['阿秋', '欧尼oni', '苏玖芷', 'AAA.柴柴阿华田', 'Jisoo', '橙子味的蛋卷🍊', '"孤注一掷.柠曦妤"', 'jssss', '不想洗头', '小红薯CDF2389', '海云 Angel_ Vision 📷', 'ment: {\'comment_id\': \'63be690e000000001d0295fc\', \'create_time\': 1673423118000, \'ip_location\': None, \'note_id\': \'63bd8735000000001c036ff2\', \'content\': \'来自星星的的孩子，这样的孩子在某一方面都有极高的天分[微笑R]加油宝妈，你们会越来越好\', \'user_id\': \'5e39660d0000000001002660\', \'nickname\': "🌻I\'m a rice fan", \'avatar\': \'https://sns-avatar-qc.xhscdn.com/avatar/63c08bf8905230158df6cfbc.jpg?imageView2/2/w/120/format/jpg\', \'sub_comment_count\': \'1\', \'last_modify_ts\': 1688580198013}', 'wote', '紫月亮', '郭郭', '智慧之星', '单眼皮妇女', '江南布依', 'momo', '作词人 尹晶晶', '与众不同', 'momo', '萌萌哒', '云霞晚渡', 'Mike', '生生不息', 'Daisy', '希望的田野', '今天涂身体乳了吗', 'vingtetunjan', '梦有晨曦', '小熊软糖的wonderland🐳', 'LLi_', '。。。。', 'Mr.Kim', 'ChENYiyInG', '接骨圣手狗师妹', 'Zoooey', '梁朝伟的马子', '圣母保佑🙏', 'YJ', 'momo', 'Ytlll', 'momo', '十行', 'yeung1103', 'summeree🦊', '疯不疯的人额', '爱搭不理白小白', '海棠花溪', 'DUNE', '我不会起名', '隐隐于无烟日', '用户已注销', '曼欧尼', '拾趣造物｜赤尘软装', '开心', '二七的小狮子', '......jjjyyy', '小红薯5F61BF32', '犯困嫌疑人', '雪', '迷宫', '小红薯E54531D7', '爱穿搭，爱养猫', '万变🐱', '胖头鱼头不胖', 'Bian瘦子💐', '丹姐', '齐齐', '画画的北北', '逗号美学🔆🎨', '∩瑶∩', '小敏吖', '☔Lostmemory🎵', '王大明', '情长不过时光', '胖的眼睛看不到星人', 'Cindy Zhang', '认真搞事业的小狮子', '淡了红颜', '崽爸和Nicole酱', '还没有想好', '安妮', '一个嘤嘤怪', '甜BaBy', 'LiLy', 'REIYNIXIL', '平男姐', '凭阑悄悄', '小红薯5CFEA146', 'BLUESKY', 'huahua', '度度吖姐', '小红薯64356DF5', '陪你到世界的终结\\\\', '你的回复已超时🌈', '蓝胖子', '笨笨的书虫', '米宝当当妈', '橙开心日常', 'IKUN-201512', '酷到爆炸的栗子', 'Luojy-Z', '闷油瓶大战卫二庄（热缩）', '隆基不打算做人了', '我的玥宝宝', 'momo', '小红', '🍃', '大荒落', '福尔摩鱼鱼', 'Mille', 'momo', 'shirly', '慕鸽艺术工作室', '自闭症独立研究者金老师', 'rheia', '🌺🌱Elsie Chen Li👒🌸', '王回回', '用户已注销', '我和我那挂门把手的男朋友', 'LucyDone', 'Aquarius', '芷菲', 'A meter of sunshine', '漪弋', '幸运', '清野待经年', '西泠雪', '会离开就别靠近\\ue034', '蜡笔小曦', 'nonan', '姑舅罢', '小红薯B26A65B5', '一个小橙子', '甜豆', '👣 Judy💃', '这个名没人取', 'momo', 'KEANU_205', '是西瓜呀！', '🍅番茄炒蛋嘛🐾', '松下问彤子', 'kammy', '王可颂', '菲菲猪日常记录', '草莓', '碎碎念', '芋圆', 'Dimples：', '嗯', '胖宸妈咪', 'SoniaGuo', '太阳家的', '彩云易散琉璃脆', 'usagitsukino', 'MaLili', '雨后的彩虹', '用户已注销', 'amomo', '貌美如花生', '哈妮', '如人饮水', '诗人苏城', '嗯', '小綿羊', '不困不困', '李好嘛', 'zy', '旎旎', '杨杨', '小语', '海布里的天空', '青槿', '帽帽和兔兔', '姑氖氖', '分肉', 'ෆ⃛YoYoᙏ̤̫͚', '虾球真好吃', '米小 Sun', 'Simona爱美式', '自己转租', '该吃水果了', '小夏乐呵呵', '一沐', '黄樱啼啼', 'Ttian', '甜甜圈圈', 'YooLaun', '铠，霖', '好吧', '满心欢喜', '满心欢喜', '梅茜减肥卡卡卡', '雨林', 'Chromium', 'xingmi', 'sun', '冰可乐']

for i in users:
    print("https://www.xiaohongshu.com/user/profile/"+comments[i])
""""  
    if comments[i][-2] in users:
        user_dic[comments[i][-2]] = comments[i][-1]
for i in users:
    print(i)
    """