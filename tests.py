# Объединение баз данных ()
# steam_games = pd.read_csv('steam_games.csv')
# steam_prices = pd.read_csv('steam_prices.csv')
# merged_df = pd.merge(steam_games, steam_prices, on='Title', how='inner')  # inner join, чтобы оставить только совпадающие игры
# print(merged_df[['Title','genres','Original Price']])
# merged_df.to_csv('my_steam_data.csv', index=False)