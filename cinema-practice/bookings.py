def add_booking(bookings, sessions, halls):
    if len(sessions) == 0:
        print("Сначала создайте хотя бы один сеанс.")
        return

    print("\nДоступные сеансы:")

    for session in sessions:
        print(
            f'ID: {session["id"]} | '
            f'Дата: {session["date"]} | '
            f'Время: {session["time"]}'
        )

    try:
        session_id = int(input("Введите ID сеанса: "))
    except ValueError:
        print("ID сеанса должен быть числом.")
        return

    selected_session = None

    for session in sessions:
        if session["id"] == session_id:
            selected_session = session
            break

    if selected_session is None:
        print("Сеанс с таким ID не найден.")
        return

    selected_hall = None

    for hall in halls:
        if hall["id"] == selected_session["hall_id"]:
            selected_hall = hall
            break

    if selected_hall is None:
        print("Кинозал для этого сеанса не найден.")
        return

    customer_name = input("Введите имя клиента: ").strip()

    if customer_name == "":
        print("Имя клиента не может быть пустым.")
        return

    try:
        row = int(input("Введите номер ряда: "))
        seat = int(input("Введите номер места: "))
    except ValueError:
        print("Номер ряда и места должен быть числом.")
        return

    if row < 1 or row > selected_hall["rows"]:
        print("Такого ряда в этом зале нет.")
        return

    if seat < 1 or seat > selected_hall["seats_per_row"]:
        print("Такого места в этом ряду нет.")
        return

    for booking in bookings:
        if (
            booking["session_id"] == session_id
            and booking["row"] == row
            and booking["seat"] == seat
        ):
            print("Это место уже забронировано на выбранный сеанс.")
            return

    if len(bookings) == 0:
        booking_id = 1
    else:
        booking_id = max(booking["id"] for booking in bookings) + 1

    booking = {
        "id": booking_id,
        "session_id": session_id,
        "customer_name": customer_name,
        "row": row,
        "seat": seat
    }

    bookings.append(booking)
    print("Место успешно забронировано.")


def show_bookings(bookings, sessions):
    if len(bookings) == 0:
        print("Бронирований пока нет.")
        return

    print("\nСписок бронирований:")

    for booking in bookings:
        session_info = "Сеанс не найден"

        for session in sessions:
            if session["id"] == booking["session_id"]:
                session_info = f'{session["date"]} {session["time"]}'
                break

        print(
            f'ID бронирования: {booking["id"]} | '
            f'Клиент: {booking["customer_name"]} | '
            f'Сеанс: {session_info} | '
            f'Ряд: {booking["row"]} | '
            f'Место: {booking["seat"]}'
        )


def cancel_booking(bookings):
    if len(bookings) == 0:
        print("Нет бронирований для отмены.")
        return

    show_bookings(bookings, [])

    try:
        booking_id = int(input("Введите ID бронирования для отмены: "))
    except ValueError:
        print("ID бронирования должен быть числом.")
        return

    for booking in bookings:
        if booking["id"] == booking_id:
            bookings.remove(booking)
            print("Бронирование отменено.")
            return

    print("Бронирование с таким ID не найдено.")