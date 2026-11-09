

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CreateCompletionResponseObject(enum.StrEnum):
    """
    The object type, which is always "text_completion"
    """

    TEXT_COMPLETION = "text_completion"

    def visit(self, text_completion: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateCompletionResponseObject.TEXT_COMPLETION:
            return text_completion()
