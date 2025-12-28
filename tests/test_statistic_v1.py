import pytest
import allure
from data.item_data import INVALID_SELLER_IDS


@allure.epic("Avito Internship API")
@allure.feature("Statistic")
@allure.story("Get statistic v1")
class TestStatisticV1:

    @allure.title("Получение статистики по объявлению (v1) — BUG: create")
    @pytest.mark.xfail(reason="BUG: POST /api/1/item returns 400")
    def test_get_statistic_v1_success(self, item_api, created_item):
        item_id = created_item["id"]
        response = item_api.get_statistic_v1(item_id)
        assert response.status_code == 200
        stats = response.json()
        assert isinstance(stats, list)
        assert len(stats) == 1
        stat = stats[0]
        assert isinstance(stat["likes"], int)
        assert isinstance(stat["viewCount"], int)
        assert isinstance(stat["contacts"], int)

    @allure.title("Получение статистики по несуществующему объявлению (v1)")
    def test_get_statistic_v1_not_found(self, item_api):
        response = item_api.get_statistic_v1("999999999999")
        assert response.status_code in (400, 404)

    @allure.title("Получение статистики с некорректным item ID (v1)")
    @pytest.mark.parametrize(
        "invalid_id",
        INVALID_SELLER_IDS,
        ids=["string_id", "negative_id", "null_id", "empty_id"]
    )
    def test_get_statistic_v1_invalid_id(self, item_api, invalid_id):
        response = item_api.get_statistic_v1(invalid_id)
        assert response.status_code in (400, 404)
