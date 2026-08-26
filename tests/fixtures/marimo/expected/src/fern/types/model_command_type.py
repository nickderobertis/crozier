

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelCommandType(enum.StrEnum):
    MODEL = "model"

    def visit(self, model: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelCommandType.MODEL:
            return model()
