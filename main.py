import pandas as pd

games_df = pd.read_csv('steam_games_db')
prices_df = pd.read_csv('prices.csv')

merged_df = pd.merge(steam_games_db, steam_prices_df, on='name_of_game', how='inner')