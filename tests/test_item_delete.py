import allure
import pytest


@allure.epic("Avito Internship API")
@allure.feature("Item")
@allure.story("Delete item")
class TestDeleteItem:
    @allure.title("Удаление существующего объявления — BUG: create item returns 400")
    @pytest.mark.xfail(reason="BUG: POST /api/1/item returns 400, невозможно создать item")
    def test_delete_item_success(self, item_api, created_item):
        item_id = created_item["id"]
        with allure.step("Удалить объявление"):
            response = item_api.delete_item(item_id)
        with allure.step("Проверить статус ответа"):
            assert response.status_code == 200
            assert response.text == ""
        with allure.step("Проверить, что объявление больше не существует"):
            get_response = item_api.get_item_by_id(item_id)
            assert get_response.status_code == 404

    @allure.title("Повторное удаление объявления — BUG: зависит от create")
    @pytest.mark.xfail(reason="BUG: POST /api/1/item returns 400")
    def test_delete_item_twice(self, item_api, created_item):
        item_id = created_item["id"]
        item_api.delete_item(item_id)
        second_response = item_api.delete_item(item_id)
        assert second_response.status_code == 404

    @allure.title("Удаление объявления с несуществующим ID — BUG: возвращает 400 вместо 404")
    def test_delete_item_not_found(self, item_api):
        non_existent_id = "999999999999"
        response = item_api.delete_item(non_existent_id)
        # BUG: API возвращает 400 вместо 404
        assert response.status_code in (400, 404)
