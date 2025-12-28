import pytest
import allure
from data.item_data import INVALID_ITEM_PAYLOADS
from api.item_api import ItemAPI

class TestCreateItem:
    @pytest.mark.xfail(reason="BUG: API returns 400 for valid create item payload")
    def test_create_item_success(self,item_api, valid_item_payload):
        response = item_api.create_item(valid_item_payload)
        assert response.status_code == 200
        body = response.json()
        assert body["sellerID"] == valid_item_payload["sellerID"]
        assert body["name"] == valid_item_payload["name"]
        assert body["price"] == valid_item_payload["price"]
        assert "createdAt" in body

    @allure.title("Создание объявления с некорректным payload")
    @pytest.mark.parametrize("invalid_payload", INVALID_ITEM_PAYLOADS)
    def test_create_item_invalid_payload(self, item_api, invalid_payload):
        response = item_api.create_item(invalid_payload)
        assert response.status_code == 400
