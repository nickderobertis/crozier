

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ListModelsResponseObject(enum.StrEnum):
    LIST = "list"

    def visit(self, list_: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListModelsResponseObject.LIST:
            return list_()
