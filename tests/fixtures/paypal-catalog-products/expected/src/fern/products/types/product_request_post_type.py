

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ProductRequestPostType(enum.StrEnum):
    """
    The product type. Indicates whether the product is physical or digital goods, or a service.
    """

    PHYSICAL = "PHYSICAL"
    DIGITAL = "DIGITAL"
    SERVICE = "SERVICE"

    def visit(
        self,
        physical: typing.Callable[[], T_Result],
        digital: typing.Callable[[], T_Result],
        service: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ProductRequestPostType.PHYSICAL:
            return physical()
        if self is ProductRequestPostType.DIGITAL:
            return digital()
        if self is ProductRequestPostType.SERVICE:
            return service()
