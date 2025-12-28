VALID_ITEM_BASE = {
    "sellerId": None,
    "name": "Test item",
    "price": 1000,
    "statistics": {
        "likes": 0,
        "viewCount": 0,
        "contacts": 0
    }
}

INVALID_ITEM_PAYLOADS = [
    {},
    {"name": "Test item"},
    {"price": 1000},
    {"sellerId": "abc", "name": "Test", "price": 1000},
    {"sellerId": 123, "name": "Test", "price": -100},
    {
        "sellerId": 123,
        "name": "Test",
        "price": 1000,
        "statistics": {
            "likes": -1,
            "viewCount": 0,
            "contacts": 0
        }
    }
]

INVALID_SELLER_IDS = [
    "abc",
    "",
    None,
    -1
]
