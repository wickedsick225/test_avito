from api.base_api import BaseAPI


class ItemAPI(BaseAPI):

    CREATE_ITEM = "/api/1/item"
    GET_ITEM = "/api/1/item/{item_id}"
    GET_ITEMS_BY_SELLER = "/api/1/{seller_id}/item"
    DELETE_ITEM = "/api/2/item/{item_id}"
    STATISTIC_V1 = "/api/1/statistic/{item_id}"
    STATISTIC_V2 = "/api/2/statistic/{item_id}"

    def create_item(self, payload):
        return self.post(self.CREATE_ITEM, json=payload)

    def get_item_by_id(self, item_id):
        return self.get(self.GET_ITEM.format(item_id=item_id))

    def get_items_by_seller(self, seller_id):
        return self.get(self.GET_ITEMS_BY_SELLER.format(seller_id=seller_id))

    def delete_item(self, item_id):
        return self.delete(self.DELETE_ITEM.format(item_id=item_id))

    def get_statistic_v1(self, item_id):
        return self.get(self.STATISTIC_V1.format(item_id=item_id))

    def get_statistic_v2(self, item_id):
        return self.get(self.STATISTIC_V2.format(item_id=item_id))
