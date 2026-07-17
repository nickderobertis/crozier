

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CatalogObjectType(enum.StrEnum):
    """
    Possible types of CatalogObjects returned from the Catalog, each
    containing type-specific properties in the `*_data` field corresponding to the object type.
    """

    ITEM = "ITEM"
    IMAGE = "IMAGE"
    CATEGORY = "CATEGORY"
    ITEM_VARIATION = "ITEM_VARIATION"
    TAX = "TAX"
    DISCOUNT = "DISCOUNT"
    MODIFIER_LIST = "MODIFIER_LIST"
    MODIFIER = "MODIFIER"
    PRICING_RULE = "PRICING_RULE"
    PRODUCT_SET = "PRODUCT_SET"
    TIME_PERIOD = "TIME_PERIOD"
    MEASUREMENT_UNIT = "MEASUREMENT_UNIT"
    SUBSCRIPTION_PLAN = "SUBSCRIPTION_PLAN"
    ITEM_OPTION = "ITEM_OPTION"
    ITEM_OPTION_VAL = "ITEM_OPTION_VAL"
    CUSTOM_ATTRIBUTE_DEFINITION = "CUSTOM_ATTRIBUTE_DEFINITION"
    QUICK_AMOUNTS_SETTINGS = "QUICK_AMOUNTS_SETTINGS"

    def visit(
        self,
        item: typing.Callable[[], T_Result],
        image: typing.Callable[[], T_Result],
        category: typing.Callable[[], T_Result],
        item_variation: typing.Callable[[], T_Result],
        tax: typing.Callable[[], T_Result],
        discount: typing.Callable[[], T_Result],
        modifier_list: typing.Callable[[], T_Result],
        modifier: typing.Callable[[], T_Result],
        pricing_rule: typing.Callable[[], T_Result],
        product_set: typing.Callable[[], T_Result],
        time_period: typing.Callable[[], T_Result],
        measurement_unit: typing.Callable[[], T_Result],
        subscription_plan: typing.Callable[[], T_Result],
        item_option: typing.Callable[[], T_Result],
        item_option_val: typing.Callable[[], T_Result],
        custom_attribute_definition: typing.Callable[[], T_Result],
        quick_amounts_settings: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CatalogObjectType.ITEM:
            return item()
        if self is CatalogObjectType.IMAGE:
            return image()
        if self is CatalogObjectType.CATEGORY:
            return category()
        if self is CatalogObjectType.ITEM_VARIATION:
            return item_variation()
        if self is CatalogObjectType.TAX:
            return tax()
        if self is CatalogObjectType.DISCOUNT:
            return discount()
        if self is CatalogObjectType.MODIFIER_LIST:
            return modifier_list()
        if self is CatalogObjectType.MODIFIER:
            return modifier()
        if self is CatalogObjectType.PRICING_RULE:
            return pricing_rule()
        if self is CatalogObjectType.PRODUCT_SET:
            return product_set()
        if self is CatalogObjectType.TIME_PERIOD:
            return time_period()
        if self is CatalogObjectType.MEASUREMENT_UNIT:
            return measurement_unit()
        if self is CatalogObjectType.SUBSCRIPTION_PLAN:
            return subscription_plan()
        if self is CatalogObjectType.ITEM_OPTION:
            return item_option()
        if self is CatalogObjectType.ITEM_OPTION_VAL:
            return item_option_val()
        if self is CatalogObjectType.CUSTOM_ATTRIBUTE_DEFINITION:
            return custom_attribute_definition()
        if self is CatalogObjectType.QUICK_AMOUNTS_SETTINGS:
            return quick_amounts_settings()
