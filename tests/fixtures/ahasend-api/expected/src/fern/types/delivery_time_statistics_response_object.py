

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DeliveryTimeStatisticsResponseObject(enum.StrEnum):
    """
    Object type identifier
    """

    LIST = "list"

    def visit(self, list_: typing.Callable[[], T_Result]) -> T_Result:
        if self is DeliveryTimeStatisticsResponseObject.LIST:
            return list_()
