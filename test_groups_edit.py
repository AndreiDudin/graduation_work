from time import sleep

from settings import token, version, group_id, token_wall,admin_token
import allure


def test_check_group_description_value_after_update(vk_api):
    vk_api.groups_edit(additional_params={'description': 'Новое описание сообщества8'})
    answer = vk_api.groups_getById(additional_params={'fields': 'description'}).json()
    description = answer['response'][0]['description']
    assert description == 'Новое описание сообщества8', f"Актуальное название {description}"


def test_modify_GroupName_value(vk_api):
    vk_api.groups_edit(additional_params={'title': 'Новое имя сообщества3'})
    name = vk_api.groups_getById(additional_params={'fields': 'title'}).json()['response'][0]['name']
    assert name == "Новое имя сообщества3"
    vk_api.groups_edit(additional_params={'title': 'Страница для тестирования'})



