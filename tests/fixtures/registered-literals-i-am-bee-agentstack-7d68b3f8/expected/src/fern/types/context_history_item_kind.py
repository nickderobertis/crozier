

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ContextHistoryItemKind(enum.StrEnum):
    MESSAGE = "message"
    ARTIFACT = "artifact"

    def visit(self, message: typing.Callable[[], T_Result], artifact: typing.Callable[[], T_Result]) -> T_Result:
        if self is ContextHistoryItemKind.MESSAGE:
            return message()
        if self is ContextHistoryItemKind.ARTIFACT:
            return artifact()
