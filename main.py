import pandas

credits_data = pandas.read_csv(r'datasets/tmdb_5000_credits.csv')
movies_data = pandas.read_csv(r'datasets/tmdb_5000_movies.csv')

while (True):
    menu = int(input(
        '\nType in one of the numbers below to choose one of options to get the recommended movies in that category:\n1.Language\n2.Genre\n3.Keywords\n4.Cast\n5.Crew\n6.Less than this many minutes\nInput:'))
    if (menu == 1):
        ln = input("Enter the language of the movie \nInput:")
        temp_df = movies_data.loc[
            movies_data['original_language'] == ln, ['original_language', 'title', 'vote_average', 'popularity',
                                                     'homepage']]  # locate rows where genre value matches genre value inputted by user, grab genre, name, popularity
        temp_df = temp_df.sort_values(by='vote_average', ascending=False)  # sort by popularity descending
        print(temp_df.head())  # print first 5 rows

    elif (menu == 2):
        print(
            "Please select a genre you prefer\n Action - type 1\nAdventure - type 2\nFantasy - type 3\nScience Fiction - type 4\nCrime - type 5\nDrama - type 6\nThriller - type 7\nAnimation - type 8\nFamily - type 9\nWestern - type 10\nComedy - type 11\nRomance - type 12\nHorror - type 13\nMystery - type 14\nWar - type 15\nHistory - type 16\nMusic - type 17\nDocumentary - type 18\nForeign - type 19\nTV Movie - type 20\n")
        check = input("Input:")
        if (check == '1'):
            genre = 'Action'
        if (check == '2'):
            genre = 'Adventure'
        if (check == '3'):
            genre = 'Fantasy'
        if (check == '4'):
            genre = 'Science Fiction'
        if (check == '5'):
            genre = 'Crime'
        if (check == '6'):
            genre = 'Drama'
        if (check == '7'):
            genre = 'Thriller'
        if (check == '8'):
            genre = 'Animation'
        if (check == '9'):
            genre = 'Family'
        if (check == '10'):
            genre = 'Western'
        if (check == '11'):
            genre = 'Comedy'
        if (check == '12'):
            genre = 'Romance'
        if (check == '13'):
            genre = 'Horror'
        if (check == '14'):
            genre = 'Mystery'
        if (check == '15'):
            genre = 'War'
        if (check == '16'):
            genre = 'History'
        if (check == '17'):
            genre = 'Music'
        if (check == '18'):
            genre = 'Documentary'
        if (check == '19'):
            genre = 'Foreign'
        if (check == '20'):
            genre = 'TV Movie'

        movies_data['genres'] = movies_data['genres'].apply(eval)  # convert genres column to lists
        genre_df = movies_data.explode('genres')  # explode the list so each entry in list becomes a new column
        genre_df.dropna(inplace=True)  # drop nan values
        genre_df['genres'] = [genre['name'] for genre in
                              genre_df['genres']]  # replace each genre value in row with the name value in the dict
        temp_df = genre_df.loc[genre_df['genres'] == genre, ['genres', 'title', 'vote_average', 'popularity',
                                                             'homepage']]  # locate rows where genre value matches genre value inputted by user, grab genre, name, popularity
        temp_df = temp_df.sort_values(by='vote_average', ascending=False)  # sort by popularity descending
        print(temp_df.head())  # print first 5 rows

    elif (menu == 3):
        print("Please input a keyword")
        keyword = input("Input:")
        movies_data['keywords'] = movies_data['keywords'].apply(eval)
        keyword_df = movies_data.explode('keywords')
        keyword_df.dropna(inplace=True)
        keyword_df['keywords'] = [keyword['name'] for keyword in keyword_df['keywords']]
        temp_df = keyword_df.loc[
            keyword_df['keywords'] == keyword, ['keywords', 'title', 'vote_average', 'popularity', 'homepage']]
        temp_df = temp_df.sort_values(by='vote_average', ascending=False)
        print(temp_df.head())

    elif (menu == 4):
        print("Please input a actors full name")
        cast = input("Input:")
        credit_data['cast'] = credit_data['cast'].apply(eval)
        cast_df = credit_data.explode('cast')
        cast_df.dropna(inplace=True)
        cast_df['cast'] = [cast['name'] for cast in cast_df['cast']]
        temp_df = cast_df.loc[cast_df['cast'] == cast, ['cast', 'title']]
        final = movies_data.merge(temp_df, on=['title'])
        final = final[['cast', 'title', 'vote_average', 'popularity', 'homepage']]
        final = final.sort_values(by='vote_average', ascending=False)
        print(final.head())

    elif (menu == 5):
        print("Please input a crew mates full name (i.e. Director full name)")
        crew = input("Input:")
        credit_data['crew'] = credit_data['crew'].apply(eval)
        crew_df = credit_data.explode('crew')
        crew_df.dropna(inplace=True)
        crew_df['crew'] = [crew['name'] for crew in crew_df['crew']]
        temp_df = crew_df.loc[crew_df['crew'] == crew, ['crew', 'title']]
        final = movies_data.merge(temp_df, on=['title'])
        final = final[['crew', 'title', 'vote_average', 'popularity', 'homepage']]
        final = final.sort_values(by='vote_average', ascending=False)
        print(final.head())

    elif (menu == 6):
        time = int(input("Enter the amount of minutes the movie should be less than: \nInput:"))
        temp_df = movies_data.loc[movies_data['runtime'] < time, ['runtime', 'title', 'vote_average', 'popularity',
                                                                  'homepage']]  # locate rows where genre value matches genre value inputted by user, grab genre, name, popularity
        temp_df = temp_df[movies_data['runtime'] != 0].sort_values(by='vote_average',
                                                                   ascending=False)  # sort by popularity descending
        print(temp_df.head())  # print first 5 rows

    else:
        break