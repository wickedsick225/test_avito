import pytest
import allure
from data.item_data import INVALID_SELLER_IDS


@allure.epic("Avito Internship API")
@allure.feature("Item")
@allure.story("Get item by id")
class TestGetItemById:

    @allure.title("Получение объявления по валидному ID — BUG: create")
    @pytest.mark.xfail(reason="BUG: create item endpoint returns 400")
    def test_get_item_by_id_success(self, item_api, created_item):
        item_id = created_item["id"]
        response = item_api.get_item_by_id(item_id)
        assert response.status_code == 200

    @allure.title("Получение объявления по несуществующему ID")
    def test_get_item_by_id_not_found(self, item_api):
        response = item_api.get_item_by_id("999999999999")
        assert response.status_code == 400 

    @allure.title("Получение объявления с некорректным ID")
    @pytest.mark.parametrize("invalid_id", INVALID_SELLER_IDS)
    def test_get_item_by_id_invalid_id(self, item_api, invalid_id):
        response = item_api.get_item_by_id(invalid_id)
        assert response.status_code in (400, 404)
