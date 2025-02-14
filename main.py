import pandas as pd
import config
import ast


steam_games_df = pd.read_csv('data_frames/steam_games_df.csv')

# def main():
#     n = 0
#     price_all = 0
#     for index, row in steam_games_df.iterrows():
#         if row['is_released'] is True and 'Indie'in row['genres']:
#             print([row['name'], row['price(USD)'], True])
#             n+=1
#             price = row['price(USD)']
#             price_all = price_all + price
#         else:
#             print([row['name'], row['price(USD)'], False])

#     print(f"Количество игр в жанре Indie: {n}")
#     print(f"{round(price_all, 2)}$")

# if __name__ == "__main__":
#     main()

steam_games_df = pd.read_csv('data_frames/steam_games_df.csv')
all_genres = config.ALL_GENRES

def main():
    
    genre_stats = {genre: {'count': 0, 'revenue': 0.0} for genre in all_genres}
    n = 0
    price_all = 0
    for index, row in steam_games_df.iterrows():
        if row['is_released'] is True:
            price = row['price(USD)']
            game_genres = ast.literal_eval(row['genres'])

        for genre in all_genres:
            if genre in game_genres:
                genre_stats[genre]['count'] += 1
                genre_stats[genre]['revenue'] += price
                
                
    for genre, stats in genre_stats.items():
        if stats['count'] > 0:
            print(f"Жанр: {genre}")
            print(f"Количество игр: {stats['count']}")
            print(f"Общий доход: {round(stats['revenue'], 2)}$")
            print("-" * 30)
    
    # Получаем строки, которые являются дубликатами по столбцу 'name'
    duplicates_df = steam_games_df[steam_games_df.duplicated(subset='name', keep=False)]

    # Выводим результат
    print(duplicates_df)

if __name__ == "__main__":
    main()