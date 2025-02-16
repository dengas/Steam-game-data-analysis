import pandas as pd
import config
import ast
from plotly_settings import plotly_settings
import time

steam_games_df = pd.read_csv('data_frames/merged_data.csv')

# Получение множества уникальных тэгов (жанров)
def unique_tags():
    tags_set = set()

    for index, row in steam_games_df.iterrows():
        tags_list = ast.literal_eval(row['tags'])
        for tags in tags_list:
            tags_set.add(tags)

    print(tags_set)

# Запись количества игр в жанре и их цен в словарь tags_counts
def main():
    tags_set = config.ALL_TAGS
    
    tags_counts = {tag : {'count': 0, 'price': 0} for tag in tags_set}
    for index, row in steam_games_df.iterrows():
        for tag in tags_set:
            if tag in ast.literal_eval(row['tags']):
                tags_counts[tag]['count'] += 1
                try:
                    tags_counts[tag]['price'] += float(row['price(USD)'].replace("$", "").replace("Free", "0"))
                except:
                    print(index, row['Title'], row['price(USD)'])

    for tag, data in tags_counts.items():
        sum_of_tags = data['count'] + 1
        total_revenue = round(data['price'], 2)
        average_revenue = round(total_revenue/sum_of_tags, 2)
        # print(f"Количество игр по тэгу {tag}: {sum_of_tags}")
        # print(f"Общая стоимость игр по тэгу {tag}: {total_revenue}$")
        # print(f"Средняя выручка по тэгу {tag}: {average_revenue}")
        # print("-" * 50)
    
    config.TAGS_DICT = tags_counts

# Создание нового dataframe - my_tags_data.csv
def my_tags_data():
    new_data = []
    for tag, data in config.TAGS_DICT.items():
        tag_name = tag
        sum_of_tags = data['count'] + 1
        total_revenue = round(data['price'], 2)
        average_revenue = round(total_revenue/sum_of_tags, 2)
        
        new_data.append({
        'name of tag': tag_name,
        'sum of tags': sum_of_tags,
        'total revenue' : total_revenue,
        'average revenue' : average_revenue
        })
    
    my_tags_data = pd.DataFrame(new_data)
    my_tags_data.to_csv('data_frames/my_tags_data.csv', index=False)

    print("Данные успешно записаны в my_tags_data.csv")
        

if __name__ == "__main__":
    start_time = time.time()
    
    # unique_tags()
    main()
    # plotly_settings()
    my_tags_data()
    
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Код выполнялся {execution_time:.2f} секунд")