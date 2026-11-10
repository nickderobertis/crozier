

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DeleteAssistantResponseObject(enum.StrEnum):
    ASSISTANT_DELETED = "assistant.deleted"

    def visit(self, assistant_deleted: typing.Callable[[], T_Result]) -> T_Result:
        if self is DeleteAssistantResponseObject.ASSISTANT_DELETED:
            return assistant_deleted()
