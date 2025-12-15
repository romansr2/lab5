class Name:
    def __init__(self, name, hobby=None) -> None:
        allowed = ["Богдан", "Анонім", "Микола"]
        if name not in allowed:
            raise ValueError("Дозволені імена: Богдан, Анонім, Микола")
        if hobby is None or (isinstance(hobby, str) and hobby.strip() == ""):
            raise ValueError("Потрібно вказати хоббі (поле не може бути пустим)")
        self.name = name
        self.hobby = hobby


if __name__ == '__main__':
    try:
        a = Name("Бодько", hobby="футбол")
    except ValueError as e:
        print('ValueError:', e)
