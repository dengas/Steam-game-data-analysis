# Объединение баз данных ()
# steam_games = pd.read_csv('steam_games.csv')
# steam_prices = pd.read_csv('steam_prices.csv')
# merged_df = pd.merge(steam_games, steam_prices, on='Title', how='inner')  # inner join, чтобы оставить только совпадающие игры
# print(merged_df[['Title','genres','Original Price']])
# merged_df.to_csv('my_steam_data.csv', index=False)
import pandas as pd
import ast



# Получение уникальных жанров
# steam_games_df = pd.read_csv('data_frames/steam_games_df.csv')

# genres_set = set()

# for index, row in steam_games_df.iterrows():
#     genres_list = ast.literal_eval(row['genres'])
#     # print(genres_list)
#     # print(type(genres_list))
#     for genres in genres_list:
#         genres_set.add(genres)

# all_genres_list = list(genres_set)

# print(all_genres_list)


# ['Racing', 'Indie', 'Massively Multiplayer', 'Photo Editing', 'Action', 'Movie', 'Casual', 'Free To Play', 'Web Publishing', 'Design & Illustration', 'Utilities', 'Documentary', 'Audio Production', 'Software Training', 'Early Access', 'Simulation', 'Short', 'Tutorial', 'Gore', '360 Video', 'Game Development', 'Sexual Content', 'Episodic', 'Adventure', 'Education', 'Animation & Modeling', 'Accounting', 'Sports', 'Violent', 'Nudity', 'Strategy', 'Video Production', 'RPG']

all_genres = ['Racing', 'Indie', 'Action', 'Adventure']
genre_counts = {genre: {'count': 0, 'price': 0} for genre in all_genres}

print(genre_counts)
