

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BrandRegistrationsEnumBrandFeedback(enum.StrEnum):
    TAX_ID = "TAX_ID"
    STOCK_SYMBOL = "STOCK_SYMBOL"
    NONPROFIT = "NONPROFIT"
    GOVERNMENT_ENTITY = "GOVERNMENT_ENTITY"
    OTHERS = "OTHERS"

    def visit(
        self,
        tax_id: typing.Callable[[], T_Result],
        stock_symbol: typing.Callable[[], T_Result],
        nonprofit: typing.Callable[[], T_Result],
        government_entity: typing.Callable[[], T_Result],
        others: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BrandRegistrationsEnumBrandFeedback.TAX_ID:
            return tax_id()
        if self is BrandRegistrationsEnumBrandFeedback.STOCK_SYMBOL:
            return stock_symbol()
        if self is BrandRegistrationsEnumBrandFeedback.NONPROFIT:
            return nonprofit()
        if self is BrandRegistrationsEnumBrandFeedback.GOVERNMENT_ENTITY:
            return government_entity()
        if self is BrandRegistrationsEnumBrandFeedback.OTHERS:
            return others()
