def MovieTimeCal(flight_length, movie_lengths : list) -> bool:
    movie_length_seen = set()
    for first_movie_length in movie_lengths:
        second_movie = flight_length - first_movie_length
        if second_movie in movie_length_seen:
            return True
        movie_length_seen.add(first_movie_length)
    return False

print(MovieTimeCal(60,[30,40,70,80,150,10]))
