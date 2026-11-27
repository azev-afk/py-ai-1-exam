def add_hall(halls):
    name = input("Введите название кинозала: ").strip()

    if name == "":
        print("Название зала не может быть пустым.")
        return

    try:
        rows = int(input("Введите количество рядов: "))
        seats_per_row = int(input("Введите количество мест в каждом ряду: "))
    except ValueError:
        print("Количество рядов и мест должно быть числом.")
        return

    if rows <= 0 or seats_per_row <= 0:
        print("Количество рядов и мест должно быть положительным.")
        return

    if len(halls) == 0:
        hall_id = 1
    else:
        hall_id = max(hall["id"] for hall in halls) + 1

    hall = {
        "id": hall_id,
        "name": name,
        "rows": rows,
        "seats_per_row": seats_per_row
    }

    halls.append(hall)
    print("Кинозал успешно добавлен.")


def show_halls(halls):
    if len(halls) == 0:
        print("Список кинозалов пуст.")
        return

    print("\nСписок кинозалов:")

    for hall in halls:
        capacity = hall["rows"] * hall["seats_per_row"]

        print(
            f'ID: {hall["id"]} | '
            f'Название: {hall["name"]} | '
            f'Рядов: {hall["rows"]} | '
            f'Мест в ряду: {hall["seats_per_row"]} | '
            f'Всего мест: {capacity}'
        )