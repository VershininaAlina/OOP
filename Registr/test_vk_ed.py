
import pytest

#Тест 1
#Проверка , что слова одинаково читается слева направо и наоборот (Является Палиндромом )
def test_Palindrom():
    s =  "Казак"
    s = s.lower()
    assert  s[:] == s[::-1], f"Данное слово не является палиндромом {s[:] } != {s[::-1]} "

# Тест 2
#Проверяем выход за индекс строки
def test_str_should_fail_out_of_bounds():
    src = "Hello, world!"
    try:
        char = src[100]
    except IndexError:
        pass

# Тест 3
#Проверить все логины пользователей
# При условии:
# Содержит 1 знак "@" и точку, которая находится после знака "@"

@pytest.mark.parametrize("login", [("qwerty@rambler.ru"), ("test@mail.ru")])
def test_check_format_login(login):
    assert ("@" in login) and ("." in login), "Не все обязательные символы содержаться в логие, проверьте условия еще раз"
    assert login.index('@') < login.index('.'), "логин должен содержать символ точки «.» после символа «@»."



# Тест 4
#Проверка граничных значение
#Два поля должны содержать числа от 6.00 (Включительно) до 12.00 (Включительно )

@pytest.mark.parametrize("a, b", [(6.00, 12.00), (6.01, 11.59)])
def test_check_boundary(a, b):

    assert (12.01 > a > 5.99) and (12.01 > b > 5.99) , f"Поля должны содержать числа от 6.00(Включительно) до 12.00 (Включительно ), " \
                                            f"ваши значения: a = {a}, b = {b}"


# Тест 5
#Проверка сложения несовместимых типов
def test_sum_float():
    a = "s"
    b = 5.66
    try:
        suma = a + b
    except TypeError:
        print("Вы сложили значения несовместимых типов")


# Тест 6
@pytest.mark.parametrize("input", [1.23, 5.660393535, 6.132523, .1, 5.0])
def test_hex_encode_decode(input):
    hex = input.hex()
    assert input == float.fromhex(hex)
