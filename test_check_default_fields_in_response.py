import pytest
import allure
from group_fields import fields

@allure.feature('Наличие обязательных полей в ответе метода groups.getById')
@pytest.mark.parametrize(
    "field_name", fields
)
def test_check_field_is_present(vk_api, field_name):
    response = vk_api.groups_getById().json()
    field = response['response'][0][field_name]
    with allure.step(f'Проверка наличия в ответе обязательного поля "{field_name}"'):
        assert field
