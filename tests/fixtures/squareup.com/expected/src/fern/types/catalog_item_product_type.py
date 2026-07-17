

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CatalogItemProductType(enum.StrEnum):
    """
    The type of a CatalogItem. Connect V2 only allows the creation of `REGULAR` or `APPOINTMENTS_SERVICE` items.
    """

    REGULAR = "REGULAR"
    GIFT_CARD = "GIFT_CARD"
    APPOINTMENTS_SERVICE = "APPOINTMENTS_SERVICE"

    def visit(
        self,
        regular: typing.Callable[[], T_Result],
        gift_card: typing.Callable[[], T_Result],
        appointments_service: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CatalogItemProductType.REGULAR:
            return regular()
        if self is CatalogItemProductType.GIFT_CARD:
            return gift_card()
        if self is CatalogItemProductType.APPOINTMENTS_SERVICE:
            return appointments_service()
