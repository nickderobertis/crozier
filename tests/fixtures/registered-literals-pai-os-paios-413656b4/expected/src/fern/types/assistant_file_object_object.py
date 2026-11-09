

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AssistantFileObjectObject(enum.StrEnum):
    """
    The object type, which is always `assistant.file`.
    """

    ASSISTANT_FILE = "assistant.file"

    def visit(self, assistant_file: typing.Callable[[], T_Result]) -> T_Result:
        if self is AssistantFileObjectObject.ASSISTANT_FILE:
            return assistant_file()
