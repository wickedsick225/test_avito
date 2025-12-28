import pytest
import allure


@allure.epic("Avito Internship API")
@allure.feature("Statistic")
@allure.story("Get statistic v2")
class TestStatisticV2:
    @allure.title("Получение статистики по объявлению (v2) — BUG: create")
    @pytest.mark.xfail(reason="BUG: POST /api/1/item returns 400")
    def test_get_statistic_v2_success(self, item_api, created_item):
        item_id = created_item["id"]
        response = item_api.get_statistic_v2(item_id)
        assert response.status_code == 200
        stats = response.json()
        assert isinstance(stats, list)
        assert len(stats) == 1
        stat = stats[0]
        assert isinstance(stat["likes"], int)
        assert isinstance(stat["viewCount"], int)
        assert isinstance(stat["contacts"], int)

    @allure.title("Получение статистики по несуществующему объявлению (v2)")
    def test_get_statistic_v2_not_found(self, item_api):
        response = item_api.get_statistic_v2("999999999999")
        assert response.status_code in (400, 404)
