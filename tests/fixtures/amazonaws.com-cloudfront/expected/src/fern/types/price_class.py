

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PriceClass(enum.StrEnum):
    PRICE_CLASS100 = "PriceClass_100"
    PRICE_CLASS200 = "PriceClass_200"
    PRICE_CLASS_ALL = "PriceClass_All"

    def visit(
        self,
        price_class100: typing.Callable[[], T_Result],
        price_class200: typing.Callable[[], T_Result],
        price_class_all: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PriceClass.PRICE_CLASS100:
            return price_class100()
        if self is PriceClass.PRICE_CLASS200:
            return price_class200()
        if self is PriceClass.PRICE_CLASS_ALL:
            return price_class_all()
