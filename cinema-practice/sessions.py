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
def show_sessions(sessions, movies, halls):
    if len(sessions) == 0:
        print("Список сеансов пуст.")
        return

    print("\nРасписание сеансов:")

    for session in sessions:
        movie_name = "Неизвестный фильм"
        hall_name = "Неизвестный кинозал"

        for movie in movies:
            if movie["id"] == session["movie_id"]:
                movie_name = movie["title"]
                break

        for hall in halls:
            if hall["id"] == session["hall_id"]:
                hall_name = hall["name"]
                break

        print(
            f'ID: {session["id"]} | '
            f'Фильм: {movie_name} | '
            f'Кинозал: {hall_name} | '
            f'Дата: {session["date"]} | '
            f'Время: {session["time"]}'
        )
