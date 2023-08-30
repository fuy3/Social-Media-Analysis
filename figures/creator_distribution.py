import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data_notes = {
    'Life Experience': [4, 0, 0], 
    'Awake Public Awareness' :[4, 4, 15], 
    'Intervention' : [5, 9, 0], 
    'Family Supports' : [14, 2, 1], 
    'Symptoms': [8, 7, 0], 
    'Science Population': [2, 11, 4], 
    'Diagnosed': [3, 1, 1], 
    'Autism Study': [0, 4, 1],

}

data_videos = {
    'Life Experience' : [41, 7, 2], 
    'Awake Public Awareness': [1, 5, 2], 
    'Intervention': [6, 6, 1], 
    'Family Supports': [7, 0, 1], 
    'Symptoms': [7, 2, 0], 
    'Science Population': [2, 2, 2], 
    'Diagnosed': [6, 0, 0], 
    'Autism Study': [0, 0, 0],

}

# 创建DataFrame
df_notes = pd.DataFrame(data_notes, index=['Autsics Relatives', 'HCPs', 'Others'])
df_videos = pd.DataFrame(data_videos, index=['Autsics Relatives', 'HCPs', 'Others'])

# 设置颜色列表
#colors = sns.color_palette("muted").as_hex()
colors = ['#E63946', '#E76F51', '#F4A261', '#F1FAEE', '#A8DADC', '#457B9D', '#1D3557', '#2A9D8F']

# 计算每个柱子的百分比
bars_height_notes = df_notes.div(df_notes.sum(axis=1), axis=0) * 100
bars_height_videos = df_videos.div(df_videos.sum(axis=1), axis=0) * 100

# 绘制横向百分比堆积图
fig, ax = plt.subplots()
y = np.arange(len(df_notes.index))
height = 0.3  # 柱子高度

# 绘制notes的柱子
left_notes = np.zeros(len(df_notes.index))
for i, col in enumerate(df_notes.columns):
    ax.barh(y + height / 2, bars_height_notes[col], height, left=left_notes, label=f"Notes-{col}", color=colors[i])
    left_notes += bars_height_notes[col]

# 绘制videos的柱子
left_videos = np.zeros(len(df_videos.index))
for i, col in enumerate(df_videos.columns):
    ax.barh(y - height / 2, bars_height_videos[col], height, left=left_videos, label=f"Videoss-{col}",color=colors[i], alpha=0.7)
    left_videos += bars_height_videos[col]

# 设置纵轴刻度和标签
ax.set_yticks(y)
ax.set_yticklabels(df_notes.index)

# 设置图表标题和标签
plt.title('Creator Identity Distribution under Different Topic in Notes or Videos')
plt.xlabel("Creator's Identity Proportion (%)")

# 添加图例
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, bbox_to_anchor=(1, 1), loc='upper left')

# 调整布局，以避免图例和图表重叠
plt.tight_layout(rect=[0, 0, 1.25, 0.6])

# 显示图表
plt.show()

