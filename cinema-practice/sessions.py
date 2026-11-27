def add_session(sessions, movies, halls):
    for movie in movies:
        print(f'ID: {movie["id"]} | {movie["title"]}')

    try:
        movie_id = int(input("Введите ID фильма: "))
    except ValueError:
        print("ID фильма должен быть числом.")
        return

    selected_movie = None

    for movie in movies:
        if movie["id"] == movie_id:
            selected_movie = movie
            break

    if selected_movie is None:
        print("Фильм с таким ID не найден.")
        return

    print("\nДоступные кинозалы:")

    for hall in halls:
        print(f'ID: {hall["id"]} | {hall["name"]}')

    try:
        hall_id = int(input("Введите ID кинозала: "))
    except ValueError:
        print("ID кинозала должен быть числом.")
        return

    selected_hall = None

    for hall in halls:
        if hall["id"] == hall_id:
            selected_hall = hall
            break
