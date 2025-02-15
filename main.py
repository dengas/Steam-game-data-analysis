import pandas as pd
import config
import ast
from plotly_settings import plotly_settings
import time

steam_games_df = pd.read_csv('data_frames/merged_data.csv')

# Получение множества уникальных тэгов (жанров)
def unique_genres():
    genres_set = set()

    for index, row in steam_games_df.iterrows():
        genres_list = ast.literal_eval(row['genres'])
        for genres in genres_list:
            genres_set.add(genres)

    print(genres_set)

# Запись количества игр в жанре и их цен в словарь genres_counts
def main():
    genres_set = config.ALL_GENRES
    
    genres_counts = {genre: {'count': 0, 'price': 0} for genre in genres_set}
    for index, row in steam_games_df.iterrows():
        for genre in genres_set:
            if genre in ast.literal_eval(row['genres']):
                genres_counts[genre]['count'] += 1
                try:
                    genres_counts[genre]['price'] += float(row['price(USD)'].replace("$", "").replace("Free", "0"))
                except:
                    print(index, row['Title'], row['price(USD)'])

    for genre, data in genres_counts.items():
        genres_counts[genre]['price'] = round(genres_counts[genre]['price'], 2)
        print(f"Количество игр в жанре {genre}: {data['count'] + 1}")
        print(f"Общая стоимость игр в жанре {genre}: {round(data['price'], 2)}$")
        print("-" * 50)
    
    config.GENRES_DICT = genres_counts


if __name__ == "__main__":
    start_time = time.time()
    # unique_genres()
    main()
    plotly_settings()
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Код выполнялся {execution_time:.2f} секунд")