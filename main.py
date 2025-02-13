import pandas as pd


# Объединение баз данных ()
# steam_games = pd.read_csv('steam_games.csv')
# steam_prices = pd.read_csv('steam_prices.csv')
# merged_df = pd.merge(steam_games, steam_prices, on='Title', how='inner')  # inner join, чтобы оставить только совпадающие игры
# print(merged_df[['Title','genres','Original Price']])
# merged_df.to_csv('my_steam_data.csv', index=False)

my_steam_data = pd.read_csv('data_frames/my_steam_data.csv')

def main():
    for index, row in my_steam_data.iterrows():
        title_genres_list = [index, row['Title'], row['Genres']]
        # print(title_genres_list[2])
        if 'Indie'in title_genres_list[2]:
            print([title_genres_list[1], True])
        else:
            print([title_genres_list[1], False])
        

    # n = 0
    # for genres in my_steam_data['Genres']:
    #     if 'Indie' in genres:
    #         print(True)
            
    # print(n)

if __name__ == "__main__":
    main()