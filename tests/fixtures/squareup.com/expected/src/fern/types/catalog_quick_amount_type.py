

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CatalogQuickAmountType(enum.StrEnum):
    """
    Determines the type of a specific Quick Amount.
    """

    QUICK_AMOUNT_TYPE_MANUAL = "QUICK_AMOUNT_TYPE_MANUAL"
    QUICK_AMOUNT_TYPE_AUTO = "QUICK_AMOUNT_TYPE_AUTO"

    def visit(
        self,
        quick_amount_type_manual: typing.Callable[[], T_Result],
        quick_amount_type_auto: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CatalogQuickAmountType.QUICK_AMOUNT_TYPE_MANUAL:
            return quick_amount_type_manual()
        if self is CatalogQuickAmountType.QUICK_AMOUNT_TYPE_AUTO:
            return quick_amount_type_auto()
