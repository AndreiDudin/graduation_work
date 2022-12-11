import allure
import json


@allure.feature('Операции с комментариями к постам')
@allure.story('Создание комментария на стене')
@allure.title('Комментарий на кириллице. В ответе возвращается айди созданного комментария')
def test_check_creating_comment_on_cirillic(vk_api):
    with allure.step('Создание нового поста'):
        create_post = vk_api.create_post_on_wall(
            additional_params={'attachments': 'photo5474852_457247970'}
        ).text
    with allure.step('Берем айдишник созданного на стене поста'):
        new_post_id = json.loads(create_post.replace("'", '"'))['response']['post_id']
    with allure.step('Берем айдишник комментария'):
        comment = vk_api.wall_createComment(new_post_id, additional_params={'message': 'Текст кириллицей'}).json()
    comment_id = comment['response']['comment_id']
    with allure.step('Проверка, что поле Id содержит значение айдишника комментария'):
        assert comment_id


@allure.feature('Операции с комментариями к постам')
@allure.story('Создание комментария на латинице. В ответе возвращаетя айди созданного комментария')
def test_check_creating_comment_on_latin(vk_api):
    with allure.step('Создание нового поста'):
        create_post = vk_api.create_post_on_wall(
            additional_params={'attachments': 'photo5474852_457247970'}
        ).text
    with allure.step('Берем айдишник созданного на стене поста'):
        new_post_id = json.loads(create_post.replace("'", '"'))['response']['post_id']
    with allure.step('Проверка, что поле Id содержит значение айдишника комментария'):
        comment = vk_api.wall_createComment(new_post_id, additional_params={'message': 'Latin text'}).json()
    comment_id = comment['response']['comment_id']
    assert comment_id


@allure.feature('Операции с комментариями к постам')
@allure.story('Создание комментария с картинкой. В ответе возвращается айди созданного комментария')
def test_check_creating_comment_with_photo(vk_api):
    with allure.step('Создание нового поста'):
        create_post = vk_api.create_post_on_wall(
            additional_params={'attachments': 'photo5474852_457247970'}
        ).text
    with allure.step('Берем айдишник созданного на стене поста'):
        new_post_id = json.loads(create_post.replace("'", '"'))['response']['post_id']
    with allure.step('Создаем комментарий и берем его айдишник'):
        comment = vk_api.wall_createComment(
            new_post_id,
            additional_params={'attachments': 'photo5474852_457247884'}).json()
    comment_id = comment['response']['comment_id']
    with allure.step('Проверка, что поле Id содержит значение айдишника комментария'):
        assert comment_id


@allure.feature('Операции с комментариями к постам')
@allure.story('Создание комментария с двумя картинками. В ответе возвращается айди созданного комментария')
def test_check_creating_comment_with_two_photos(vk_api):
    with allure.step('Создание нового поста'):
        create_post = vk_api.create_post_on_wall(
            additional_params={'attachments': 'photo5474852_457247970'}
        ).text
    with allure.step('Берем айдишник созданного на стене поста'):
        new_post_id = json.loads(create_post.replace("'", '"'))['response']['post_id']

    with allure.step('Создаем комментарий и берем его айдишник'):
        comment = vk_api.wall_createComment(new_post_id, additional_params={
            'attachments': 'photo5474852_457247884,photo5474852_457247821'}).json()
    comment_id = comment['response']['comment_id']
    with allure.step('Проверка, что поле Id содержит значение айдишника комментария'):
        assert comment_id


@allure.feature('Операции с комментариями к постам')
@allure.story('Создание комментария с видео. В ответе возвращается айди созданного комментария')
def test_check_creating_comment_with_video(vk_api):
    with allure.step('Создание нового поста'):
        create_post = vk_api.create_post_on_wall(
            additional_params={'attachments': 'photo5474852_457247970'}
        ).text
    with allure.step('Берем айдишник созданного на стене поста'):
        new_post_id = json.loads(create_post.replace("'", '"'))['response']['post_id']
    with allure.step('Создаем комментарий с видео и берем его айдишник'):
        comment = vk_api.wall_createComment(new_post_id, additional_params={
            'attachments': 'video-42793953_456242346'}).json()
    comment_id = comment['response']['comment_id']
    with allure.step('Проверка, что поле Id содержит значение айдишника комментария'):
        assert comment_id


@allure.feature('Операции с комментариями к постам')
@allure.story('Создание комментария с видео. Проверка, что тип аттачмента "video"')
@allure.title('Проверка, что у комментария с видео тип аттачмента = "video"')
def test_check_creating_post_with_only_photo(vk_api):
    with allure.step('Создание нового поста'):
        create_post = vk_api.create_post_on_wall(
            additional_params={'attachments': 'photo5474852_457247970'}
        ).text
    with allure.step('Берем айдишник созданного на стене поста'):
        new_post_id = json.loads(create_post.replace("'", '"'))['response']['post_id']
    with allure.step('Создаем комментарий и берем его айдишник'):
        comment_id = vk_api.wall_createComment(
            new_post_id,
            additional_params={
            'attachments': 'video-42793953_456242346'}).json()['response']['comment_id']
#    comment_id = comment['response']['comment_id']
    comment_fields = vk_api.wall_getComment(comment_id).json()
    attachment_type = comment_fields['response']['items'][0]['attachments'][0]['video']['type']
    with allure.step('Проверка, что тип аттачмента - "video"'):
        assert attachment_type == 'video'

@allure.feature('Операции с комментариями к постам')
@allure.story('Создание комментария на стене')
@allure.title('Проверка, что созданный к посту комментарий содержит правильный текст')
def test_check_comment_text(vk_api):
    with allure.step('Создание нового поста'):
        create_post = vk_api.create_post_on_wall(
            additional_params={'attachments': 'photo5474852_457247970',
                               'message': 'Текст к видео'}).text
    with allure.step('Берем айдишник созданного на стене поста'):
        new_post_id = json.loads(create_post.replace("'", '"'))['response']['post_id']
    with allure.step('Публикуем комментарий к посту и берем из ответа сервера его айдишник'):
        comment_id = vk_api.wall_createComment(
            new_post_id,
            additional_params={'message': 'Текст комментария'}
        ).json()['response']['comment_id']
    comment_text = vk_api.wall_getComment(comment_id).json()['response']['items'][0]['text']
    assert comment_text == 'Текст комментария'

