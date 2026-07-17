

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EcommerceProductStatus(enum.StrEnum):
    """
    The current status of the product (active or archived).
    """

    ACTIVE = "active"
    ARCHIVED = "archived"

    def visit(self, active: typing.Callable[[], T_Result], archived: typing.Callable[[], T_Result]) -> T_Result:
        if self is EcommerceProductStatus.ACTIVE:
            return active()
        if self is EcommerceProductStatus.ARCHIVED:
            return archived()
