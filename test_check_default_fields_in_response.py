import pytest
from settings import token, version, group_id
import allure
from group_fields import fields

@pytest.mark.parametrize(
    "field_name", fields
)
def test_check_field_is_present(vk_api, field_name):
    response = vk_api.groups_getById().json()
    field = response['response'][0][field_name]
    assert field