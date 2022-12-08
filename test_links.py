from time import sleep
from settings import token, version, group_id, token_wall, admin_token
import allure


@allure.feature('Ссылки в группе')
@allure.story('Успешное создание. Проверка имени созданной ссылки')
@allure.title('В ответе возвращается верное значение в поле "name"')
def test_link_name(vk_api):
    with allure.step('Добавление ссылки'):
        response = vk_api.groups_addLink(additional_params={
            'link': 'https://www.mail.ru',
            'text': 'почта'}).json()
    with allure.step('Проверяем, что имя ссылки = "почта"'):
        name = response['response']['name']
    assert name == 'почта', f"Актуальное имя {response['response']['name']}"


@allure.feature('Ссылки в группе')
@allure.story('Успешное создание. Проверка описания созданной ссылки')
@allure.title('Значение поля "desc" = "www.mail.ru"')
def test_check_link_description(vk_api):
    with allure.step('Добавление ссылки'):
        response = vk_api.groups_addLink(additional_params={
            'link': 'https://www.mail.ru',
            'text': 'mail.ru'}).json()
    with allure.step('Проверяем, что описание ссылки = "www.mail.ru"'):
        desc = response['response']['desc']
    assert desc == 'www.mail.ru', f"Актуальное описание {response['response']['desc']}"


@allure.feature('Ссылки в группе')
@allure.story('Успешное создание. Проверка урла созданной ссылки')
@allure.title('В ответе возвращается url созданной ссылки')
def test_check_link_url(vk_api):
    with allure.step('Добавление ссылки'):
        response = vk_api.groups_addLink(additional_params={
            'link': 'https://www.mail.ru',
            'text': 'mail.ru'}).json()
    with allure.step('Проверяем, что описание ссылки = "mail.ru"'):
        desc = response['response']['url']
    assert desc == 'https://www.mail.ru', f"Актуальная ссылка {response['response']['url']}"


@allure.feature('Ссылки в группе')
@allure.story('Обязательные/необязательные параметры в запросе.')
@allure.title('Успешное создание ссылки при отсутствии необязательного параметра "text"')
def test_check_link_id(vk_api):
    with allure.step('Добавление ссылки'):
        response = vk_api.groups_addLink(additional_params={
            'link': 'https://www.mail.ru'}).json()
    with allure.step('Проверяем, что в ответе передается id созданной ссылки'):
        assert response['response']['id'], f"Актуальная ссылка {response['response']['url']}"


@allure.feature('Ссылки в группе')
@allure.story('Обязательные/необязательные параметры в запросе')
@allure.title('Ответ с кодом 100 при отсутствии в запросе параметра "link"')
def test_without_link_check_code_100(vk_api):
    with allure.step('Добавление ссылки'):
        response = vk_api.groups_addLink(additional_params={
            'text': 'mail.ru'}).json()
    with allure.step('Проверяем, что в ответе получаем код 100'):
        assert response['error']['error_code'] == 100


@allure.feature('Ссылки в группе')
@allure.story('Обязательные/необязательные параметры в запросе')
@allure.title('Ответ с кодом 100 при отсутствии в запросе параметров')
def test_without_params_check_code_100(vk_api):
    with allure.step('Добавление ссылки без параметров'):
        response = vk_api.groups_addLink(additional_params={}).json()
    with allure.step('Проверяем, что в ответе получаем код 100'):
        assert response['error']['error_code'] == 100