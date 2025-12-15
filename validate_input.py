def input_number_demo():
    a = input("Введіть число: ")
    assert a.isdigit(), "Потрібно ввести число!"
    print(f"введене число: {a}")


if __name__ == '__main__':
    try:
        input_number_demo()
    except AssertionError as e:
        print('AssertionError:', e)
