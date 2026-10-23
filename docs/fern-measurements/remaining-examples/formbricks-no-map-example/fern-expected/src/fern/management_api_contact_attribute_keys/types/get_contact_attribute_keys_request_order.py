

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetContactAttributeKeysRequestOrder(enum.StrEnum):
    """
    Sort order
    """

    ASC = "asc"
    DESC = "desc"

    def visit(self, asc: typing.Callable[[], T_Result], desc: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetContactAttributeKeysRequestOrder.ASC:
            return asc()
        if self is GetContactAttributeKeysRequestOrder.DESC:
            return desc()
