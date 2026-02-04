def num_to_word(words_list, answer):
    if answer:
        return words_list[answer - 1]
    return 'Некорректный ввод'

def check_user_input():
    user_input = input('Введите число от 1 до 5:\n')
    if user_input.isdigit() and int(user_input) in range(1, 6):
        return int(user_input)

def main():
    words_list = ['One', 'Two', 'Three', 'Four', 'Five']
    print(num_to_word(words_list,check_user_input()))

if __name__ == '__main__':
    main()
