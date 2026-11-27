import movies
import halls
import sessions
import bookings


def main():
    movies_list = []
    halls_list = []
    sessions_list = []
    bookings_list = []

    while True:
        print("\n===== CINEMA MANAGEMENT SYSTEM =====")
        print("1. Добавить фильм")
        print("2. Показать фильмы")
        print("3. Удалить фильм")
        print("4. Добавить кинозал")
        print("5. Показать кинозалы")
        print("6. Создать сеанс")
        print("7. Показать расписание")
        print("8. Забронировать место")
        print("9. Показать бронирования")
        print("10. Отменить бронирование")
        print("0. Выход")

        choice = input("Выберите действие: ").strip()

        if choice == "1":
            movies.add_movie(movies_list)

        elif choice == "2":
            movies.show_movies(movies_list)

        elif choice == "3":
            movies.delete_movie(movies_list)

        elif choice == "4":
            halls.add_hall(halls_list)

        elif choice == "5":
            halls.show_halls(halls_list)

        elif choice == "6":
            sessions.add_session(
                sessions_list,
                movies_list,
                halls_list
            )

        elif choice == "7":
            sessions.show_sessions(
                sessions_list,
                movies_list,
                halls_list
            )

        elif choice == "8":
            bookings.add_booking(
                bookings_list,
                sessions_list,
                halls_list
            )

        elif choice == "9":
            bookings.show_bookings(
                bookings_list,
                sessions_list
            )

        elif choice == "10":
            bookings.cancel_booking(bookings_list)

        elif choice == "0":
            print("Программа завершена.")
            break

        else:
            print("Неверный пункт меню. Попробуйте ещё раз.")


if __name__ == "__main__":
    main()