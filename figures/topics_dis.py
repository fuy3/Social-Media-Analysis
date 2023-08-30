import matplotlib.pyplot as plt

# 数据和标签
data_notes = [4, 23, 14, 17, 15, 17, 5, 5]
data_videos = [50,8,13,8,9,6,6,0]
data = [27,15.5,13.5,12.5,12,11.5,5.5,2.5]
labels = ['Life Expirence', 'Public Awarenes', 'Intervention', 'Family Supports', 'Symptoms', 'Science Population', 'Diagnosed', 'Autism Study']

# 新的莫兰迪色系的颜色代码
new_morandi_colors = ['#E63946', '#F1FAEE', '#A8DADC', '#457B9D', '#1D3557', '#F4A261', '#2A9D8F', '#E76F51']

# 绘制扇形图
fig, ax = plt.subplots()
ax.pie(data, labels=labels, autopct='%1.1f%%', startangle=90, colors=new_morandi_colors, textprops={'fontsize': 17})
# 获取图表的坐标轴
ax.axis('equal')  # 保证图表是圆形的

# 添加标题
plt.text(0, -1.3, '(c) Overall Topis Distribution', ha='center', fontsize=20)

# 显示图表
plt.show()

