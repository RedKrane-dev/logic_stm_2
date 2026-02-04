def num_to_word(words_list: list[str], answer: int) -> str:
    """
    - Принимает список доступных слов-чисел
    - Возвращает слово соответсвующее введенному числу
    """
    if answer:
        return words_list[answer - 1]
    return 'Некорректный ввод'

def check_user_input(min_num: int, max_num: int) -> int:
    """
    - Принимает минимальное/максимальное значения для выбора
    - Запрашивает ввод пользователя и валидирует его.
    - Возвращает целочисленное
    """
    while True:
        try:
            user_input = int(input(f'Введите число от {min_num} до {max_num}:\n'))
            if user_input and min_num <= user_input <= max_num:
                return user_input
            else:
                print('Некорректный ввод\n')
        except ValueError:
            print('Некорректный ввод\n')

def main():
    """
    Исполняемая функция программы
    """
    words_list = ['One', 'Two', 'Three', 'Four', 'Five']
    max_num = len(words_list)
    print(num_to_word(words_list, check_user_input(min_num=1, max_num=max_num)))

if __name__ == '__main__':
    main()
