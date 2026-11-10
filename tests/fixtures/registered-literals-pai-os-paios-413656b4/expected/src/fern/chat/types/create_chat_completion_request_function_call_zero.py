

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateChatCompletionRequestFunctionCallZero(enum.StrEnum):
    """
    `none` means the model will not call a function and instead generates a message. `auto` means the model can pick between generating a message or calling a function.
    """

    NONE = "none"
    AUTO = "auto"

    def visit(self, none: typing.Callable[[], T_Result], auto: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateChatCompletionRequestFunctionCallZero.NONE:
            return none()
        if self is CreateChatCompletionRequestFunctionCallZero.AUTO:
            return auto()
