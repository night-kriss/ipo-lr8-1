import json
import os

filename = 'cities.json'

def initialize_data():
    if not os.path.exists(filename):
        data = [
            {"id": 1, "name": "Минск", "country": "Беларусь", "is_big": True, "people_count": 2000000},
            {"id": 2, "name": "Москва", "country": "Россия", "is_big": True, "people_count": 12500000},
            {"id": 3, "name": "Киев", "country": "Украина", "is_big": True, "people_count": 2800000},
            {"id": 4, "name": "Вильнюс", "country": "Литва", "is_big": False, "people_count": 500000},
            {"id": 5, "name": "Рига", "country": "Латвия", "is_big": False, "people_count": 700000}
        ]
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

def load_data():
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_data(data):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def display_all_records():
    data = load_data()
    for record in data:
        print(f"ID: {record['id']}, Название: {record['name']}, Страна: {record['country']}, "
              f"Большой город: {record['is_big']}, Население: {record['people_count']}")

def display_record_by_id():
    search_id = input("Введите ID записи: ")
    if not search_id.isdigit():
        print("Некорректный ввод. ID должно быть числом.")
        return
    search_id = int(search_id)
    data = load_data()
    found = False
    for index, record in enumerate(data):
        if record['id'] == search_id:
            print(f"=============== Найдено ===============")
            print(f"Позиция: {index}, ID: {record['id']}, Название: {record['name']}, Страна: {record['country']}, "
                  f"Большой город: {record['is_big']}, Население: {record['people_count']}")
            found = True
            break
    if not found:
        print("=============== Не найдено ===============")

def add_record():
    new_id = input("Введите ID: ")
    if not new_id.isdigit():
        print("Некорректный ввод. ID должно быть числом.")
        return
    new_id = int(new_id)
    new_name = input("Введите название города: ")
    new_country = input("Введите название страны: ")
    new_is_big = input("Является ли город большим (True/False): ").lower()
    if new_is_big not in ['true', 'false']:
        print("Некорректный ввод. Введите True или False.")
        return
    new_is_big = new_is_big == 'true'
    new_people_count = input("Введите население города: ")
    if not new_people_count.isdigit():
        print("Некорректный ввод. Население должно быть числом.")
        return
    new_people_count = int(new_people_count)
    new_record = {
        "id": new_id,
        "name": new_name,
        "country": new_country,
        "is_big": new_is_big,
        "people_count": new_people_count
    }
    data = load_data()
    data.append(new_record)
    save_data(data)
    print("Запись добавлена.")

def delete_record_by_id():
    delete_id = input("Введите ID записи для удаления: ")
    if not delete_id.isdigit():
        print("Некорректный ввод. ID должно быть числом.")
        return
    delete_id = int(delete_id)
    data = load_data()
    new_data = [record for record in data if record['id'] != delete_id]
    if len(new_data) == len(data):
        print("=============== Не найдено ===============")
    else:
        save_data(new_data)
        print("Запись удалена.")

def main():
    initialize_data()
    operations_count = 0

    while True:
        print("\nМеню:")
        print("1. Вывести все записи")
        print("2. Вывести запись по полю")
        print("3. Добавить запись")
        print("4. Удалить запись по полю")
        print("5. Выйти из программы")
        
        choice = input("Выберите пункт меню: ")

        if choice == '1':
            display_all_records()
            operations_count += 1

        elif choice == '2':
            display_record_by_id()
            operations_count += 1

        elif choice == '3':
            add_record()
            operations_count += 1

        elif choice == '4':
            delete_record_by_id()
            operations_count += 1

        elif choice == '5':
            print(f"Количество выполненных операций: {operations_count}")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
