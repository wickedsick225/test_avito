from api.base_api import BaseAPI


class StatisticAPI(BaseAPI):

    def get_stat_v1(self, item_id):
        return self.get(self.GET_STAT_V1.format(item_id=item_id))

    def get_stat_v2(self, item_id):
        return self.get(self.GET_STAT_V2.format(item_id=item_id))