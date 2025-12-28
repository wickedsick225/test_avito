import pytest
import random
import copy
from api.item_api import ItemAPI
from data.item_data import VALID_ITEM_BASE


@pytest.fixture(scope="session")
def seller_id():
    return random.randint(111111, 999999)


@pytest.fixture
def item_api():
    return ItemAPI()

@pytest.fixture
def valid_item_payload(seller_id):
    payload = copy.deepcopy(VALID_ITEM_BASE)
    payload["sellerID"] = seller_id
    return payload


@pytest.fixture
def created_item(item_api, valid_item_payload):
    response = item_api.create_item(valid_item_payload)
    assert response.status_code == 200
    return response.json()
