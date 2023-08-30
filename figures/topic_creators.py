import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data_notes = {
    'relatives': [14, 4, 4, 0, 3, 8, 2, 5],
    'HCPs': [2, 0, 4, 4, 1, 7, 11, 9],
    'others': [1, 0, 15, 1, 1, 0, 4, 0],
}

data_videos = {
    'relatives': [7, 41, 1, 0, 6, 7, 2, 6],
    'HCPs': [0, 7, 5, 0, 0, 2, 2, 6],
    'others': [1, 2, 2, 0, 0, 0, 2, 1],
}

# 创建DataFrame
df_notes = pd.DataFrame(data_notes, index=['Family Supports', 'Life Expirence', 'Public Awarness', 'Autsim Study', 'Diagnosed', 'Symptoms', 'Science Population', 'Intervention'])
df_videos = pd.DataFrame(data_videos, index=['Family Supports', 'Life Expirence', 'Public Awarness', 'Autsim Study', 'Diagnosed', 'Symptoms', 'Science Population', 'Intervention'])


# 设置颜色列表
#colors = ['blue', 'green', 'red', 'purple', 'orange']
colors = sns.color_palette("muted").as_hex()

# 计算每个柱子的高度
bars_height_notes = df_notes.values
bars_height_videos = df_videos.values

# 绘制柱状图
fig, ax = plt.subplots()
x = np.arange(len(df_notes.index))
width = 0.25  # 柱子宽度

# 绘制notes的柱状图
bottom = np.zeros(len(df_notes.index))
for i, col in enumerate(df_notes.columns):
    ax.bar(x, bars_height_notes[:, i], width, bottom=bottom, label=col, color=colors[i])
    bottom += bars_height_notes[:, i]

# 绘制videos的柱状图
bottom = np.zeros(len(df_notes.index))
for i, col in enumerate(df_videos.columns):
    ax.bar(x + width, bars_height_videos[:, i], width, bottom=bottom, color=colors[i])
    bottom += bars_height_videos[:, i]

# 设置横轴刻度和标签
ax.set_xticks(x + width / 2)
ax.set_xticklabels(df_notes.index)

# 设置图表标题和标签
plt.title('Distribution Relationship Between Post Topics and Creator Identities')
#plt.xlabel('contents')
plt.ylabel("Creator's Identitie / Proportation")

# 添加图例
ax.legend()

# 显示图表
plt.show()

