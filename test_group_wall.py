from time import sleep
from settings import token, version, group_id, token_wall, owner_id
import allure
import json

@allure.feature('Операции с постами на стене')
@allure.story('Работа с комбинациями аттачментов')
def test_check_creating_post_with_only_photo(vk_api):
    with allure.step('Создание нового поста'):
        create_post = vk_api.create_post_on_wall(
            additional_params={'attachments': 'photo5474852_457247970'}
        ).text
    with allure.step('Берем айдишник созданного на стене поста'):
        new_post_id = json.loads(create_post.replace("'", '"'))['response']['post_id']
    with allure.step('Берем контент созданного поста'):
        new_post_content = vk_api.wall_getById(f"-{group_id}_{new_post_id}").json()
    photo_info=new_post_content['response']['items'][0]['attachments'][0]['photo']
    with allure.step('Проверка, что созданном посте есть фото'):
        assert photo_info, "Пост с фото не создался"


@allure.feature('Операции с постами на стене')
@allure.story('Публикация текста латиницей')
def test_check_latin_text_in_post(vk_api):
    with allure.step('Создание нового поста'):
        create_post = vk_api.create_post_on_wall(additional_params={'message':"Latin text"}).text
    with allure.step('Берем айдишник созданного на стене поста'):
        new_post_id = json.loads(create_post.replace("'", '"'))['response']['post_id']
    with allure.step('Берем контент созданного поста'):
        new_post_content = vk_api.wall_getById(f"-{group_id}_{new_post_id}").json()['response']['items'][0]['text']
    with allure.step('Проверка, что текст на латинском соответствует введенному при создании'):
        assert new_post_content == "Latin text"


@allure.feature('Операции с постами на стене')
@allure.story('Публикация текста кириллицей')
def test_check_cyrillic_text_in_post(vk_api):
    with allure.step('Создание нового поста'):
        create_post = vk_api.create_post_on_wall(additional_params={'message':'Текст на кириллице'}).text
    with allure.step('Берем айдишник созданного на стене поста'):
        new_post_id = json.loads(create_post.replace("'", '"'))['response']['post_id']
    with allure.step('Берем контент созданного поста'):
        new_post_content = vk_api.wall_getById(f"-{group_id}_{new_post_id}").json()['response']['items'][0]['text']
    with allure.step('Проверка, что текст на кириллице соответствует введенному при создании'):
        assert new_post_content == "Текст на кириллице"


@allure.feature('Операции с постами на стене')
@allure.story('Айди созданного поста есть в списке всех постов')
def test_check_new_post_is_added(vk_api, current_datetime):
    with allure.step('Создание нового поста'):
        create_post = vk_api.create_post_on_wall(additional_params={'message': current_datetime}).text
    with allure.step('Берем айдишник созданного на стене поста'):
        new_post_id = json.loads(create_post.replace("'", '"'))['response']['post_id']
    post_id = vk_api.wall_get().json()['response']['items']
    ids_all = []
    for id in post_id:
        ids_all.append(str(id['id']))
    with allure.step('Проверяем, что айдишник созданного поста есть в списке всех постов'):
        assert str(new_post_id) in ids_all


@allure.feature('Операции с постами на стене')
@allure.story('Айди созданного поста является первым с списке всех постов')
def test_check_new_post_is_first(vk_api,current_datetime):
    with allure.step('Создание нового поста'):
        create_post = vk_api.create_post_on_wall(additional_params={'message': current_datetime}).text
    with allure.step('Берем айдишник созданного на стене поста'):
        new_post_id = json.loads(create_post.replace("'", '"'))['response']['post_id']
    post_id = vk_api.wall_get().json()['response']['items']
    ids_all = []
    for id in post_id:
        ids_all.append(str(id['id']))
    with allure.step('Проверка, что айди созданного поста находится самым первым в списке всех постов'):
        assert str(new_post_id) == ids_all[0]


@allure.feature('Операции с постами на стене')
@allure.story('Удаление успешно созданного поста')
def test_delete_post_after_publication(vk_api,current_datetime):
    with allure.step('Создание нового поста'):
        create_post = vk_api.create_post_on_wall(additional_params={'message': current_datetime}).text
    sleep(1)
    with allure.step('Берем айдишник созданного на стене поста'):
        new_post_id = str(json.loads(create_post.replace("'", '"'))['response']['post_id'])
    post_ids = vk_api.wall_get().json()['response']['items']
    ids_all = []
    for id in post_ids:
        current_id = str(id['id'])
        ids_all.append(current_id)
    with allure.step('Проверка, что айди созданного поста находится в списке всех постов'):
        assert new_post_id in ids_all, f"New post is absent on the wall"
    with allure.step('Удаляем созданный пост'):
        vk_api.delete_post_from_wall(new_post_id).json()
    with allure.step('Собираем список всех постов на стене после удаления'):
        wall_posts_after_delete = vk_api.wall_get().json()['response']['items']
    ids_all_after = []
    for id in wall_posts_after_delete:
        current_id = str(id['id'])
        ids_all_after.append(current_id)
    with allure.step('Проверка, что айди удаленного поста нет в списке существующих'):
        assert new_post_id not in ids_all_after, f"Актуальное количество постов {wall_posts_after_delete}"
