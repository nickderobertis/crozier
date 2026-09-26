

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SkuMetaInProductType(enum.StrEnum):
    BLUE_HAT = "blue_hat"
    SPORTS = "sports"
    GENERAL_FOOD = "general_food"
    OTHER = "other"

    def visit(
        self,
        blue_hat: typing.Callable[[], T_Result],
        sports: typing.Callable[[], T_Result],
        general_food: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SkuMetaInProductType.BLUE_HAT:
            return blue_hat()
        if self is SkuMetaInProductType.SPORTS:
            return sports()
        if self is SkuMetaInProductType.GENERAL_FOOD:
            return general_food()
        if self is SkuMetaInProductType.OTHER:
            return other()
