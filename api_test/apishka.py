import requests


class Location:

    """Запрос на всех юзеров"""

    def test_list_users(self):
        print("Список пользователей\n")
        get_url = "https://reqres.in/api/users?key=?page=2"
        result_get = requests.get(get_url)
        print(result_get.text)
        print("Статус код : " + str(result_get.status_code))
        assert 200 == result_get.status_code
        if result_get.status_code == 200:
            print("Успешно!!!\n")
        else:
            print("Провал!!! Запрос ошибочный\n")
        return result_get.status_code

    """Запрос на одного юзера"""

    def test_single_user(self):
        print("Один пользователь\n")
        get_url = "https://reqres.in/api/user/2"
        result_get = requests.get(get_url)
        print(result_get.text)
        print("Статус код : " + str(result_get.status_code))
        assert 200 == result_get.status_code
        if result_get.status_code == 200:
            print("Успешно!!!\n")
        else:
            print("Провал!!! Запрос ошибочный\n")
        return result_get.status_code

    """Запрос на одного юзера с ошибкой"""

    def test_single_user_not_found(self):
        print("Один пользователь не найден\n")
        get_url = "https://reqres.in/api/users/23"
        result_get = requests.get(get_url)
        print(result_get.text)
        print("Статус код : " + str(result_get.status_code))
        assert 404 == result_get.status_code
        if result_get.status_code == 404:
            print("Успешно!!! Пользователь не найден\n")
        else:
            print("Провал!!! Запрос ошибочный\n")
        return result_get.status_code

    """Запрос на ресурсы"""

    def test_list_resource(self):
        print("Список ресурсов\n")
        get_url = "https://reqres.in/api/unknown"
        result_get = requests.get(get_url)
        print(result_get.text)
        print("Статус код : " + str(result_get.status_code))
        assert 200 == result_get.status_code
        if result_get.status_code == 200:
            print("Успешно!!!\n")
        else:
            print("Провал!!! Запрос ошибочный\n")
        return result_get.status_code

    """Запрос на один ресурс"""

    def test_single_responce(self):
        print("Один ресурс\n")
        get_url = "https://reqres.in/api/unknown/2"
        result_get = requests.get(get_url)
        print(result_get.text)
        print("Статус код : " + str(result_get.status_code))
        assert 200 == result_get.status_code
        if result_get.status_code == 200:
            print("Успешно!!!\n")
        else:
            print("Провал!!! Запрос ошибочный\n")
        return result_get.status_code

    """Запрос на один ресурс с ошибкой"""

    def test_single_respoce_not_found(self):
        print("Один ресурс не найден\n")
        get_url = "https://reqres.in/api/unknown/23"
        result_get = requests.get(get_url)
        print(result_get.text)
        print("Статус код : " + str(result_get.status_code))
        assert 404 == result_get.status_code
        if result_get.status_code == 404:
            print("Успешно!!! Ресурс не найден\n")
        else:
            print("Провал!!! Запрос ошибочный\n")
        return result_get.status_code

    """Создание нового пользователя"""

    def test_post_create(self):
        print("Создание нового пользователя:\n")

        post_url = "https://reqres.in/api/users"
        json_for_create_new_person = {
            "name": "morpheus",
            "job": "leader"
        }
        result_post = requests.post(post_url, json=json_for_create_new_person)
        print("Статус код : " + str(result_post.status_code))
        assert 201 == result_post.status_code
        if result_post.status_code == 201:
            print("Успешно!!! Создан новый пользователь")
        else:
            print("Провал!!! Запрос ошибочный")
        check_post = result_post.json()
        id_person = check_post.get("id")
        print("id : " + id_person)
        created_AT = check_post.get("createdAt")
        print("createdAt : " + created_AT)
        return result_post.status_code

    """Изменение нового пользователя через put"""

    def test_put_update(self):
        print("\nИзменение нового пользователя через put:\n")
        put_url = "https://reqres.in/api/users/2"
        json_for_update_new_person = {
            "name": "morpheus",
            "job": "zion resident"
        }
        result_put = requests.put(put_url, json=json_for_update_new_person)
        print("Статус код : " + str(result_put.status_code))
        assert 200 == result_put.status_code
        if result_put.status_code == 200:
            print("Успешно!!! Изменения нового пользователя прошло успешно")
        else:
            print("Провал!!! Запрос ошибочный")
        check_put = result_put.json()
        check_put_info = check_put.get("job")
        print("Работа : " + check_put_info)
        check_updated = check_put.get("updatedAt")
        print("Обновлено : " + check_updated)
        return result_put.status_code

    """Изменение нового пользователя через patch"""

    def test_patch_update(self):
        print("\nИзменение пользователя через patch:\n")
        patch_url = "https://reqres.in/api/users/2"
        json_for_update_new_person = {
            "name": "morpheus",
            "job": "zion resident"
        }
        result_patch = requests.patch(patch_url, json=json_for_update_new_person)
        print("Статус код : " + str(result_patch.status_code))
        assert 200 == result_patch.status_code
        if result_patch.status_code == 200:
            print("Успешно!!! Изменения пользователя прошло успешно")
        else:
            print("Провал!!! Запрос ошибочный")
        check_patch = result_patch.json()
        check_patch_info = check_patch.get("job")
        print("Работа : " + check_patch_info)
        check_updated = check_patch.get("updatedAt")
        print("Обновлено : " + check_updated)
        return result_patch.status_code

    """Удаление нового пользователя"""

    def test_delete(self):
        print("\nУдаление пользователя:\n")
        delete_url = "https://reqres.in/api/users/2"
        result_delete = requests.delete(delete_url)
        print("Статус код : " + str(result_delete.status_code))
        assert 204 == result_delete.status_code
        if result_delete.status_code == 204:
            print("Успешно!!! Удаление новой локации не возможно")
        else:
            print("Провал!!! Запрос ошибочный")
        return result_delete.status_code

    """Регистрация пользователя"""

    def test_register_successful(self):
        print("Регистрация пользователя:\n")
        post_url = "https://reqres.in/api/register"
        json_for_create_new_person = {
            "email": "eve.holt@reqres.in",
            "password": "pistol"
        }
        result_post = requests.post(post_url, json=json_for_create_new_person)
        print("Статус код : " + str(result_post.status_code))
        assert 200 == result_post.status_code
        if result_post.status_code == 200:
            print("Успешно!!! Зарегистрирован новый пользователь")
        else:
            print("Провал!!! Запрос ошибочный")
        check_post = result_post.json()
        id_person = check_post.get("id")
        print("id : " + str(id_person))
        token = check_post.get("token")
        print("token : " + token)
        return result_post.status_code

    """Регистрация пользователя с ошибкой"""

    def test_register_unseccessful(self):
        print("\nРегистрация пользователя с ошибкой:\n")
        post_url = "https://reqres.in/api/register"
        json_for_create_new_person = {
            "email": "sydney@fife"
        }
        result_post = requests.post(post_url, json=json_for_create_new_person)
        print("Статус код : " + str(result_post.status_code))
        assert 400 == result_post.status_code
        if result_post.status_code == 400:
            print("Успешно!!! Регистрация упала с ошибкой")
        else:
            print("Провал!!! Запрос ошибочный")
        check_post = result_post.json()
        id_person = check_post.get("error")
        print("id : " + id_person)
        return result_post.status_code

    """Регистрация пользователя login"""

    def test_login_successful(self):
        print("\nРегистрация пользователя login:\n")
        post_url = "https://reqres.in/api/register"
        json_for_create_new_person = {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }
        result_post = requests.post(post_url, json=json_for_create_new_person)
        print("Статус код : " + str(result_post.status_code))
        assert 200 == result_post.status_code
        if result_post.status_code == 200:
            print("Успешно!!! Зарегистрирован новый пользователь")
        else:
            print("Провал!!! Запрос ошибочный")
        check_post = result_post.json()
        token = check_post.get("token")
        print("token : " + token)
        return result_post.status_code

    """Регистрация пользователя с ошибкой login"""

    def test_login_unsuccessful(self):
        print("\nРегистрация пользователя с ошибкой login:\n")
        post_url = "https://reqres.in/api/register"
        json_for_create_new_person = {
            "email": "peter@klaven"
        }
        result_post = requests.post(post_url, json=json_for_create_new_person)
        print("Статус код : " + str(result_post.status_code))
        assert 400 == result_post.status_code
        if result_post.status_code == 400:
            print("Успешно!!! Регистрация упала с ошибкой")
        else:
            print("Провал!!! Запрос ошибочный")
        check_post = result_post.json()
        id_person = check_post.get("error")
        print("id : " + id_person)
        return result_post.status_code

    """Делей запрос 3 секунды"""

    def delayed_response(self):
        print("Список пользователей\n")
        get_url = "https://reqres.in/api/users?delay=3"
        result_get = requests.get(get_url)
        print(result_get.text)
        print("Статус код : " + str(result_get.status_code))
        assert 200 == result_get.status_code
        if result_get.status_code == 200:
            print("Успешно!!!\n")
        else:
            print("Провал!!! Запрос ошибочный\n")
        return result_get.status_code


new_place = Location()
new_place.test_post_create()
