

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetWebhooksRequestOrder(enum.StrEnum):
    """
    Sort order
    """

    ASC = "asc"
    DESC = "desc"

    def visit(self, asc: typing.Callable[[], T_Result], desc: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetWebhooksRequestOrder.ASC:
            return asc()
        if self is GetWebhooksRequestOrder.DESC:
            return desc()
