

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelUpdateMessageMethod(enum.StrEnum):
    UPDATE = "update"

    def visit(self, update: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelUpdateMessageMethod.UPDATE:
            return update()
