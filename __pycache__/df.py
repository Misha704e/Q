def show_movies():
    try:
        with open("hello.txt", "r", encoding="utf-8") as file:
            print("Привіт! Ось ваш список фільмів:")
            print(file.read())
    except FileNotFoundError:
        print("Файл 'hello.txt' не знайдено!")

def add_task():
    task = input("Яку справу додати? ")
    with open("справи.txt", "a", encoding="utf-8") as file:
        file.write(task + "\n")
    print("Справу додано!")

def view_tasks():
    try:
        with open("справи.txt", "r", encoding="utf-8") as file:
            print("Ось ваш список справ:")
            print(file.read())
    except FileNotFoundError:
        print("Файл 'справи.txt' не знайдено!")

def delete_task():
    try:
        with open("справи.txt", "r", encoding="utf-8") as file:
            tasks = file.readlines()

        print("Ваш список справ:")
        for i, task in enumerate(tasks):
            print(f"{i}: {task.strip()}")

        index = int(input("Введіть номер завдання, яке потрібно видалити: "))
        if 0 <= index < len(tasks):
            del tasks[index]
            with open("справи.txt", "w", encoding="utf-8") as file:
                file.writelines(tasks)
            print("Завдання видалено!")
        else:
            print("Неправильний номер.")
    except FileNotFoundError:
        print("Файл 'справи.txt' не знайдено!")
    except ValueError:
        print("Помилка: потрібно ввести число.")

def main():
    show_movies()

    action = input("Що ви хочете зробити? (додати/видалити/переглянути/вихід): ").lower()
    while action != "вихід":
        if action == "додати":
            add_task()
        elif action == "видалити":
            delete_task()
        elif action == "переглянути":
            view_tasks()
        else:
            print("Невідома дія, спробуйте ще раз.")

        action = input("Що ви хочете зробити? (додати/видалити/переглянути/вихід): ").lower()

if __name__ == "__main__":
    main()