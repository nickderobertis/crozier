

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DeliveryPartnerType(enum.StrEnum):
    """
    The data type
    """

    DELIVERY_PARTNER = "delivery-partner"

    def visit(self, delivery_partner: typing.Callable[[], T_Result]) -> T_Result:
        if self is DeliveryPartnerType.DELIVERY_PARTNER:
            return delivery_partner()
