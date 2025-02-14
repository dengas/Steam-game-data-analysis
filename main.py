import pandas as pd
import config
import ast



steam_games_df = pd.read_csv('data_frames/steam_games_df.csv')

def main():
    all_genres = config.ALL_GENRES
    
    genre_counts = {genre: {'count': 0, 'price': 0} for genre in all_genres}
    for index, row in steam_games_df.iterrows():
        if row['is_released'] is True:
            for genre in all_genres:
                if genre in ast.literal_eval(row['genres']):
                    genre_counts[genre]['count'] += 1
                    genre_counts[genre]['price'] += row['price(USD)']

    for genre, data in genre_counts.items():
        print(f"Количество игр в жанре {genre}: {data['count'] + 1}")
        print(f"Общая стоимость игр в жанре {genre}: {round(data['price'], 2)}$")
        print("-" * 50)

if __name__ == "__main__":
    main()