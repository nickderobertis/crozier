

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelUpdateMethod(enum.StrEnum):
    UPDATE = "update"

    def visit(self, update: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelUpdateMethod.UPDATE:
            return update()
