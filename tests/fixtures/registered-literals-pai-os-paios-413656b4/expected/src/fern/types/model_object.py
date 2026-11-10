

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelObject(enum.StrEnum):
    """
    The object type, which is always "model".
    """

    MODEL = "model"

    def visit(self, model: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelObject.MODEL:
            return model()
