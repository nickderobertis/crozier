

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelObject(enum.StrEnum):
    MODEL = "model"

    def visit(self, model: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelObject.MODEL:
            return model()
