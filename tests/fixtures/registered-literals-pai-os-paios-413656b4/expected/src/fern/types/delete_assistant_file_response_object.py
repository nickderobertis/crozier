

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DeleteAssistantFileResponseObject(enum.StrEnum):
    ASSISTANT_FILE_DELETED = "assistant.file.deleted"

    def visit(self, assistant_file_deleted: typing.Callable[[], T_Result]) -> T_Result:
        if self is DeleteAssistantFileResponseObject.ASSISTANT_FILE_DELETED:
            return assistant_file_deleted()
