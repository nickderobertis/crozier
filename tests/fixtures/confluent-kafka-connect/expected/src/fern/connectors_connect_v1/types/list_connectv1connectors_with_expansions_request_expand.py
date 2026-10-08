

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListConnectv1ConnectorsWithExpansionsRequestExpand(enum.StrEnum):
    ID = "id"
    INFO = "info"
    STATUS = "status"

    def visit(
        self,
        id: typing.Callable[[], T_Result],
        info: typing.Callable[[], T_Result],
        status: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ListConnectv1ConnectorsWithExpansionsRequestExpand.ID:
            return id()
        if self is ListConnectv1ConnectorsWithExpansionsRequestExpand.INFO:
            return info()
        if self is ListConnectv1ConnectorsWithExpansionsRequestExpand.STATUS:
            return status()
