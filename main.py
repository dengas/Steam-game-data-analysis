import pandas as pd



steam_games_df = pd.read_csv('data_frames/steam_games_df.csv')

def main():
    n = 0
    for index, row in steam_games_df.iterrows():
        if row['is_released'] is True and 'Indie'in row['genres']:
            n+=1
            print([row['name'], row['price(USD)'], True])
        else:
            print([row['name'], row['price(USD)'], False])
    print(n)

if __name__ == "__main__":
    main()