# Lab5 — Звіт лабораторної роботи: Assertions, Validation і Unit Testing

- `app.py` — клас `Figure` з властивістю та тестовою функцією `test_app_triangle`.
- `test.py` — `unittest` тести для `Figure`.
- `validate_input.py` — демонстрація вводу + `assert`.
- `name_example.py` — валідація імені та хоббі (приклад з `ValueError`).
- `requirements.txt` — dev-залежності для тестування та покриття.

**Виконання роботи**

1. Реалізовано клас `Figure` з перевіркою аргументів через `assert` та властивостями:
   - `get_figure_type` — повертає тип фігури;
   - `get_figure_length` — повертає довжину (виправлено помилку);
   - `get_angles` — повертає кількість кутів (4 для квадрата/прямокутника, 3 для трикутника).
2. Додано `unittest` тести в `test.py` та `pytest` тест у `app.py` (`test_app_triangle`).
3. Додано демонстрацію `input` + `assert` у `validate_input.py`.
4. Згенеровано звіт покриття тестів (HTML) у папці `htmlcov`.

**Результати виконання завдань**

- Створив  файли: `app.py`, `test.py`, `validate_input.py`, `name_example.py`, `.gitignore`, `requirements.txt`, `.coveragerc`.
- Програма (демо) вивела приклади валідації при неправильному вводі (див. `validate_input.py`).
- Отримано наступні результати при виконанні тестів (консольні логи):

  Початковий запуск `unittest` (до виправлення) показав помилку у властивості довжини:

  ```text
  FAILED (failures=1)
  AssertionError: 6 != 'трикутник' : Властивість get_figure_length повертає непривильну довжину!
  ```

  Після виправлення `get_figure_length` та додавання `get_angles` — повторний запуск `unittest`:

  ```text
  Ran 4 tests in 0.001s

  OK
  ```

  PyTest для `app.py`:

  ```text
  1 passed in 0.03s
  ```

  Покриття тестами (pytest-cov):

  ```text
  Name     Stmts   Miss  Cover
  ----------------------------
  app.py      23      6    74%
  ```

  HTML-звіт покриття згенеровано у `htmlcov/index.html`.

**Код (витяги)**

Фрагмент `validate_input.py`:

```python
def input_number_demo():
	a = input("Введіть число: ")
	assert a.isdigit(), "Потрібно ввести число!"
	print(f"введене число: {a}")

if __name__ == '__main__':
	try:
		input_number_demo()
	except AssertionError as e:
		print('AssertionError:', e)
```

Фрагмент кінцевого `app.py` (ключові частини):

```python
class Figure:
	FIGURES = ["квадрат", "прямокутник", "трикутник"]
	def __init__(self, type, length) -> None:
		assert length > 0, "Довжина має бути більшою за 0!"
		assert type in self.FIGURES, "Дозволені фігури: квадрат, прямокутник, трикутник"
		self.type = type
		self.length = length

	@property
	def get_figure_type(self):
		return self.type

	@property
	def get_figure_length(self):
		return self.length

	@property
	def get_angles(self):
		if self.type in ["квадрат", "прямокутник"]:
			return 4
		if self.type == "трикутник":
			return 3
```


**Результати виконання індивідуального завдання**

- Додано перевірку імен у `name_example.py` з власним іменем `Микола` у списку дозволених;
- Додано валідацію хобі (поле не пусте) і приклад виклику, який ілюструє `ValueError` при помилці.

**Інструкції для відтворення (команди)**

```powershell
py -3 -m unittest -v
py -3 -m pytest --cov=app --cov-report=html app.py
py -3 validate_input.py
```

HTML-звіт буде у `htmlcov/index.html`

**Висновок**

- Що зроблено в роботі: реалізовано клас `Figure` з валідацією аргументів, додано тести (`unittest` + `pytest`), створено приклади вводу з `assert`, згенеровано звіт покриття коду (HTML).
- Чи досягнуто мети роботи: так — продемонстровано використання `assert` для валідації, організацію юніт-тестів і збір покриття.
- Які нові знання отримано: робота з `assert`, підхід до валідації у ООП, написання тестів у `unittest` та `pytest`, використання `pytest-cov`/`coverage` для збору метрик.
- Чи вдалося відповісти на всі питання: так — усі основні завдання виконані, тести пройшли.
- Чи вдалося виконати всі завдання: так, включно з генерацією HTML-звіту покриття.
- Чи виникли складності: невелика — спочатку була навмисна помилка в `get_figure_length`, що показало корисність тестів.
- Чи подобається такий формат здачі роботи (Feedback): зручний — містить код, тести, лог і HTML-звіт.
- Побажання для покращення (Suggestions): додати автоматизацію CI (GitHub Actions) для запуску тестів і генерації coverage при кожному пуші.
