from time import sleep
from settings import token, version, group_id, token_wall, admin_token
import allure


@allure.feature('Ссылки в группе')
@allure.story('Успешное создание. Проверка имени созданной ссылки')
def test_link_name(vk_api):
    with allure.step('Добавление ссылки'):
        response = vk_api.groups_addLink(additional_params={
            'link': 'https://www.mail.ru',
            'text': 'mail.ru'}).json()
    with allure.step('Проверяем, что имя ссылки = "mail.ru"'):
        name = response['response']['name']
    assert name == 'mail.ru', f"Актуальное название {response['response']['name']}"


@allure.feature('Ссылки в группе')
@allure.story('Успешное создание. Проверка описания созданной ссылки')
def test_check_link_description(vk_api):
    with allure.step('Добавление ссылки'):
        response = vk_api.groups_addLink(additional_params={
            'link': 'https://www.mail.ru',
            'text': 'mail.ru'}).json()
    with allure.step('Проверяем, что описание ссылки = "mail.ru"'):
        desc = response['response']['desc']
    assert desc == 'www.mail.ru', f"Актуальное название {response['response']['desc']}"


@allure.feature('Ссылки в группе')
@allure.story('Успешное создание. Проверка урла созданной ссылки')
def test_check_link_url(vk_api):
    with allure.step('Добавление ссылки'):
        response = vk_api.groups_addLink(additional_params={
            'link': 'https://www.mail.ru',
            'text': 'mail.ru'}).json()
    with allure.step('Проверяем, что описание ссылки = "mail.ru"'):
        desc = response['response']['url']
    assert desc == 'https://www.mail.ru', f"Актуальное название {response['response']['url']}"
