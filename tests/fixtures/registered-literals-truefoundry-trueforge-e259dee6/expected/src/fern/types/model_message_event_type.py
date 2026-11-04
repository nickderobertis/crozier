

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelMessageEventType(enum.StrEnum):
    """
    Complete assistant model message.
    """

    MODEL_MESSAGE = "model.message"

    def visit(self, model_message: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelMessageEventType.MODEL_MESSAGE:
            return model_message()
