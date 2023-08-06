import sender_stand_request
import new_kits

# Функция для изменения значения параметра name в теле запроса
def get_kit_body(name):
    # Копируется словарь с телом запроса из файла new_kits
    current_kit_body = new_kits.kit_body.copy()
    # Изменение значения в поле name
    current_kit_body["name"] = name
    # Возвращается новый словарь с нужным значением name
    return current_kit_body
#Функция для получения токена
#def get_new_user_token():
 #   return requests.get(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
  #                       json=body,
   #                      headers=data.headers)

    #response = post_new_user(data.user_body)

# Функция для позитивной проверки
def positive_assert(kit_body):
    # В переменную kit_body сохраняется обновлённое тело запроса
    kit_body = get_kit_body(name)
    # В переменную new_product_kit_response сохраняется результат запроса на создание набора
    new_product_kits_response = sender_stand_request.post_new_product_kits(kit_body)

# Проверяется, что код ответа равен 201
    assert new_product_kits_response.status_code == 201
    # Проверяется, что в ответе есть поле name и оно не пустое
    assert kit_body.json()["name"] != ""

    # В переменную kits_table_response сохраняется результат запроса
    kits_table_response = sender_stand_request.get_kits_table()

    # Строка, которая должна быть в ответе
    str_kits = kit_body.json()["name"]

# Функция негативной проверки, когда в ответе ошибка
def negative_assert_code_400(kit_body):
    # В переменную kit_body сохраняется обновлённое тело запроса
    kit_body = get_kit_body(name)
    # В переменную kit_response сохраняется результат запроса на создание набора
    new_product_kits_response = sender_stand_request.post_new_product_kits(kit_body)

    # Проверяется, что код ответа равен 400
    assert response.status_code == 400

    # Проверяется, что в теле ответа атрибут "code" равен 400
    assert response.json()["code"] == 400
    # Проверяется текст в теле ответа в атрибуте "message"
    assert response.json()["message"] == "Не все необходимые параметры были переданы"

#Тест 1. Допустимое количество символов - 1
def test_create_kit_name_1_symbol():
    positive_assert("a")

#Тест 2. Допустимое количество символов - 511
def test_create_kit_name_511_symbol():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

#Тест 3. Количество символов меньше допустимого - 0
def test_create_kit_name_0_symbol():
    positive_assert("")

#Тест 4. Количество символов больше допустимого - 512
def test_create_kit_name_512_symbol():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

#Тест 5. Разрешены английские буквы
def test_create_kit_name_english_symbol():
    positive_assert("QWErty")

#Тест 6. Разрешены русские буквы
def test_create_kit_name_russish_symbol():
    positive_assert("Мария")

#Тест 7. Разрешены спецсимволы
def test_create_kit_name_special_symbol():
    positive_assert("№%@")

#Тест 8. Разрешены пробелы
def test_create_kit_name_with_space():
    positive_assert("Человек и КО")

#Тест 9. Разрешены цифры
def test_create_kit_name_has_number():
    positive_assert("123")

#Тест 10. Параметр не передан в запросе
def test_create_kit_name_no_name():
    # Копируется словарь с телом запроса из файла new_kits в переменную kit_body
    kit_body = new_kits.kit_body.copy()
    # Удаление параметра name из запроса
    kit_body.pop("name")
    # Проверка полученного ответа
    negative_assert_no_name(kit_body)

#Тест 11. Передан другой тип параметра
def test_create_kit_name_has_number():
    # В переменную kit_body сохраняется обновлённое тело запроса
    kit_body = get_kit_body(123)
    # В переменную kit_response сохраняется результат запроса на создание набора
    new_product_kits_response = sender_stand_request.post_new_product_kits(kit_body)

    # Проверка кода ответа
    assert response.status_code == 400