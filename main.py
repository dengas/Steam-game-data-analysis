import pandas as pd



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