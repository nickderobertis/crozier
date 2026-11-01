

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ShippingAddressAddressType(enum.StrEnum):
    """
    Type of address.
    """

    NONE = "None"
    RESIDENTIAL = "Residential"
    COMMERCIAL = "Commercial"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        residential: typing.Callable[[], T_Result],
        commercial: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ShippingAddressAddressType.NONE:
            return none()
        if self is ShippingAddressAddressType.RESIDENTIAL:
            return residential()
        if self is ShippingAddressAddressType.COMMERCIAL:
            return commercial()
