import pandas as pd
import config
import ast
from plotly_settings import plotly_settings


steam_games_df = pd.read_csv('data_frames/steam_games_df.csv')

def main():
    all_genres = config.ALL_GENRES
    
    genres_counts = {genre: {'count': 0, 'price': 0} for genre in all_genres}
    for index, row in steam_games_df.iterrows():
        if row['is_released'] is True:
            for genre in all_genres:
                if genre in ast.literal_eval(row['genres']):
                    genres_counts[genre]['count'] += 1
                    genres_counts[genre]['price'] += row['price(USD)']
                    round(genres_counts[genre]['price'], 2)

    for genre, data in genres_counts.items():
        genres_counts[genre]['price'] = round(genres_counts[genre]['price'], 2)
        print(f"Количество игр в жанре {genre}: {data['count'] + 1}")
        print(f"Общая стоимость игр в жанре {genre}: {round(data['price'], 2)}$")
        print("-" * 50)
    
    print(genres_counts)
    
    config.GENRES_DICT = genres_counts


if __name__ == "__main__":
    main()
    plotly_settings()