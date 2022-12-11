import pytest
import requests
import allure
from datetime import datetime
from settings import token, version, group_id, token_wall, owner_id, admin_token


@pytest.fixture
def vk_api():
    return ApiClient(base_address="https://api.vk.com/method")


@pytest.fixture(scope="function")
def current_datetime():
    now = datetime.now()
    return now


class ApiClient:
    def __init__(self, base_address):
        self.base_address = base_address

    # Создание комментария к посту
    def wall_createComment(self, post_id, additional_params=None):
        url = f"{self.base_address}/wall.createComment"
        params = {
            'access_token': token_wall,
            'v': version,
            'owner_id': owner_id,
            'post_id': post_id
        }
        if additional_params:
            params.update(additional_params)
        response = requests.post(url, params=params)
        return response

    # Получение информации о комментарии к посту на стене
    def wall_getComment(self, comment_id, additional_params=None):
        url = f"{self.base_address}/wall.getComment"
        params = {
            'access_token': token_wall,
            'v': version,
            'owner_id': owner_id,
            'comment_id': comment_id,
            'extended': 1
        }
        if additional_params:
            params.update(additional_params)
        response = requests.post(url, params=params)
        return response

    # Размещение поста на стене группы
    def create_post_on_wall(self, additional_params=None):
        url = f"{self.base_address}/wall.post"
        params = {
            'access_token': token_wall,
            'v': version,
            'owner_id': owner_id
        }
        if additional_params:
            params.update(additional_params)
        response = requests.post(url, params=params)
        return response

    def wall_get(self):
        url = f"{self.base_address}/wall.get"
        params = {
            'access_token': token_wall,
            'v': version,
            'owner_id': owner_id,
            'domain': group_id,
            'offset': 0,
            'count': 100,
            'filter': 'all',
            'extended': 1
        }
        response = requests.post(url, params)
        return response


    def wall_getById(self, posts):
        url = f"{self.base_address}/wall.getById"
        params = {
            'access_token': token_wall,
            'v': version,
            'posts': posts,
            'extended': 1
        }
        response = requests.post(url, params)
        return response

    def delete_post_from_wall(self, post_id):
        url = f"{self.base_address}/wall.delete"
        params = {
            'access_token': token_wall,
            'v': version,
            'owner_id': owner_id,
            'post_id': post_id
        }
        response = requests.post(url, params)
        return response

    def groups_edit(self, additional_params=None):
        url = f"{self.base_address}/groups.edit"
        params = {
            'access_token': admin_token,
            'v': version,
            'group_id': group_id
        }
        if additional_params:
            params.update(additional_params)
        response = requests.post(url, params)
        return response

    # Получение иинформации по группе по ее id
    def groups_getById(self, additional_params=None):
        url = f"{self.base_address}/groups.getById"
        params = {
            'access_token': admin_token,
            'v': version,
            'group_id': group_id
        }
        if additional_params:
            params.update(additional_params)
        response = requests.post(url, params)
        return response

    # Добавление ссылки в группу
    def groups_addLink(self, additional_params=None):
        url = f"{self.base_address}/groups.addLink"
        params = {
            'access_token': admin_token,
            'v': version,
            'group_id': 217125833
        }
        if additional_params:
            params.update(additional_params)
        response = requests.post(url, params=params)
        return response
