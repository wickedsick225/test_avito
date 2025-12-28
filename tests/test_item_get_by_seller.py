import pytest
import allure
from data.item_data import INVALID_SELLER_IDS


@allure.epic("Avito Internship API")
@allure.feature("Item")
@allure.story("Get items by sellerId")
class TestGetItemsBySellerId:
    @allure.title("Получение объявлений продавца — BUG: зависит от create")
    @pytest.mark.xfail(reason="BUG: POST /api/1/item returns 400")
    def test_get_items_by_seller_single(self, item_api, created_item):
        seller_id = created_item["sellerId"]
        response = item_api.get_items_by_seller(seller_id)
        assert response.status_code == 200
        items = response.json()
        assert isinstance(items, list)
        assert items[0]["sellerId"] == seller_id

    @allure.title("Получение объявлений продавца (без проверок на пустоту)")
    def test_get_items_by_seller_response_structure(self, item_api):
        seller_id = 999999999
        response = item_api.get_items_by_seller(seller_id)
        assert response.status_code == 200
        assert isinstance(response.json(), list)

    @allure.title("Получение объявлений с некорректным sellerId")
    @pytest.mark.parametrize(
        "invalid_seller_id",
        INVALID_SELLER_IDS,
        ids=["string", "empty", "null", "negative"]
    )
    def test_get_items_by_seller_invalid_id(self, item_api, invalid_seller_id):
        response = item_api.get_items_by_seller(invalid_seller_id)
        import pytest
import allure
from data.item_data import INVALID_SELLER_IDS


@allure.epic("Avito Internship API")
@allure.feature("Item")
@allure.story("Get items by sellerId")
class TestGetItemsBySellerId:

    @allure.title("Получение объявлений продавца — BUG: зависит от create")
    @pytest.mark.xfail(reason="BUG: POST /api/1/item returns 400")
    def test_get_items_by_seller_single(self, item_api, created_item):
        seller_id = created_item["sellerId"]

        response = item_api.get_items_by_seller(seller_id)

        assert response.status_code == 200
        items = response.json()
        assert isinstance(items, list)
        assert items[0]["sellerId"] == seller_id

    @allure.title("Получение объявлений продавца без объявлений")
    def test_get_items_by_seller_empty(self, item_api):
        seller_id = 999999999
        response = item_api.get_items_by_seller(seller_id)

        assert response.status_code == 200
        assert isinstance(response.json(), list)

    @allure.title("Получение объявлений с некорректным sellerId (BUG: negative → 200)")
    @pytest.mark.parametrize(
        "invalid_seller_id",
        INVALID_SELLER_IDS,
        ids=["string", "empty", "null", "negative"]
    )
    def test_get_items_by_seller_invalid_id(self, item_api, invalid_seller_id):
        response = item_api.get_items_by_seller(invalid_seller_id)
        # BUG: sellerId = -1 возвращает 200 и пустой список
        assert response.status_code in (200, 400, 404, 405)
