import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer
import seaborn as sns
import matplotlib.pyplot as plt
import ast

df = pd.read_csv('data_frames/merged_data.csv')

# Предположим, что у тебя есть столбцы: 'game_id', 'name', 'tags', 'revenue'
# Убедимся, что тэги в списке
df['genres'] = df['genres'].apply(ast.literal_eval)  # Если тэги сохранены как строка вида ['Action','RPG']

# Бинаризуем тэги
mlb = MultiLabelBinarizer()
tags_df = pd.DataFrame(mlb.fit_transform(df['genres']), columns=mlb.classes_)

# Объединяем с исходными данными
df = pd.concat([df, tags_df], axis=1)

# Считаем корреляцию
tag_corr = df.corr(numeric_only=True)[['price(USD)']].drop(index='price(USD)')

print(tag_corr)


plt.figure(figsize=(8, 6))
sns.heatmap(tag_corr, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Корреляция между тэгами и выручкой')
plt.show()