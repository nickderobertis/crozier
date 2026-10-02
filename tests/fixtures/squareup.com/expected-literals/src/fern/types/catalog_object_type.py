

import typing

CatalogObjectType = typing.Union[
    typing.Literal[
        "ITEM",
        "IMAGE",
        "CATEGORY",
        "ITEM_VARIATION",
        "TAX",
        "DISCOUNT",
        "MODIFIER_LIST",
        "MODIFIER",
        "PRICING_RULE",
        "PRODUCT_SET",
        "TIME_PERIOD",
        "MEASUREMENT_UNIT",
        "SUBSCRIPTION_PLAN",
        "ITEM_OPTION",
        "ITEM_OPTION_VAL",
        "CUSTOM_ATTRIBUTE_DEFINITION",
        "QUICK_AMOUNTS_SETTINGS",
    ],
    typing.Any,
]
