print("Привіт ось ваш список фільмів які ви хотіли переглянути")
todo_list=open("hello.txt", "r")
# Читаємо файл
read_content = todo_list.read()
print(read_content)
#########################################################
# Запит на додавання завдання
answer = input("Чи бажаєте ви додати якісь плани? (так/ні): ").lower()
if answer == "так":
        task = input("Яку справу додати? ")
        with open('hello.txt', "a", encoding="utf-8") as file:
            file.write(task + "\n")
        print("Справу додано!")
else:
        print("Окей.")
# Запит на видалення завдання
        answer = input("Чи бажаєте ви видалити якісь плани? (так/ні): ").lower()
        if answer == "так":
            try:
                task_index = int(input("Введіть індекс того, що хочете видалити:\n"))
                if 0 <= task_index < len(todo_list):
                    removed_task = todo_list.pop(task_index)
                    with open('hello.txt', "w", encoding="utf-8") as file:
                        file.writelines(todo_list)
                    print(f"Справу '{removed_task.strip()}' видалено!")
                else:
                    print("Неправильний індекс.")
            except ValueError:
                print("Помилка: індекс має бути числом.")
        else:
            print("Окей.")
    
# Запит на перегляд списку
answer3 = input('Чи бажаєте ви переглянути список планів? (так/ні): ').lower()
if answer3 == "так":
    print(todo_list)
else:
    print('Ну тоді все, дякую!')