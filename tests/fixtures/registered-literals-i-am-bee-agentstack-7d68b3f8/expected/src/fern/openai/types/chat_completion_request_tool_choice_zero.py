

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ChatCompletionRequestToolChoiceZero(enum.StrEnum):
    NONE = "none"
    AUTO = "auto"
    REQUIRED = "required"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        auto: typing.Callable[[], T_Result],
        required: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ChatCompletionRequestToolChoiceZero.NONE:
            return none()
        if self is ChatCompletionRequestToolChoiceZero.AUTO:
            return auto()
        if self is ChatCompletionRequestToolChoiceZero.REQUIRED:
            return required()
