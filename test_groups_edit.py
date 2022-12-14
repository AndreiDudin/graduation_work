import allure

version = '5.131'
group_id = '217125833'
owner_id = '-217125833'

@allure.feature('Редактирование параметров группы')
@allure.title('Изменение описания сообщества')
def test_check_group_description_value_after_update(vk_api):
    with allure.step('Изменение значения description'):
        vk_api.groups_edit(additional_params={'description': 'Новое описание сообщества8'})
    answer = vk_api.groups_getById(additional_params={'fields': 'description'}).json()
    with allure.step('Проверяем новое значение description'):
        description = answer['response'][0]['description']
    assert description == 'Новое описание сообщества8', f"Актуальное название {description}"
    with allure.step('Возвращаем название в первоначальное'):
        vk_api.groups_edit(additional_params={'description': 'Описание сообщества'})


@allure.feature('Редактирование параметров группы')
@allure.title('Изменение заголовка сообщества')
def test_modify_GroupName_value(vk_api):
    with allure.step("Меняем заголовок сообщества"):
        vk_api.groups_edit(additional_params={'title': 'Новое имя сообщества3'})
    with allure.step("Берем значение заголовка сообщества после изменения"):
        name = vk_api.groups_getById(
            additional_params={'fields': 'title'}
        ).json()['response'][0]['name']
    with allure.step("Проверка, что новое имя сообщества = 'Новое имя сообщества3'"):
        assert name == "Новое имя сообщества3"
    with allure.step('Возвращаем в первоначальное значение'):
        vk_api.groups_edit(additional_params={'title': 'Страница для тестирования'})


