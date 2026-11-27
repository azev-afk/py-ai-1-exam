def add_movie(movies):
    title = input("Введите название фильма: ").strip()

    if title == "":
        print("Название не может быть пустым.")
        return

    genre = input("Введите жанр фильма: ").strip()

    if genre == "":
        print("Жанр не может быть пустым.")
        return

    try:
        duration = int(input("Введите продолжительность в минутах: "))
    except ValueError:
        print("Продолжительность должна быть числом.")
        return

    if duration <= 0:
        print("Продолжительность должна быть положительным числом.")
        return

    if len(movies) == 0:
        movie_id = 1
    else:
        movie_id = max(movie["id"] for movie in movies) + 1

    movie = {
        "id": movie_id,
        "title": title,
        "genre": genre,
        "duration": duration
    }

    movies.append(movie)
    print("Фильм успешно добавлен.")


def show_movies(movies):
    if len(movies) == 0:
        print("Список фильмов пуст.")
        return

    print("\nСписок фильмов:")

    for movie in movies:
        print(
            f'ID: {movie["id"]} | '
            f'Название: {movie["title"]} | '
            f'Жанр: {movie["genre"]} | '
            f'Продолжительность: {movie["duration"]} мин.'
        )


def delete_movie(movies):
    if len(movies) == 0:
        print("Нет фильмов для удаления.")
        return

    show_movies(movies)

    try:
        movie_id = int(input("Введите ID фильма для удаления: "))
    except ValueError:
        print("ID должен быть числом.")
        return

    for movie in movies:
        if movie["id"] == movie_id:
            movies.remove(movie)
            print("Фильм удалён.")
            return

    print("Фильм с таким ID не найден.")