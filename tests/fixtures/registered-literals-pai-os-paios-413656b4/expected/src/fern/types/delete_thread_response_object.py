

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DeleteThreadResponseObject(enum.StrEnum):
    THREAD_DELETED = "thread.deleted"

    def visit(self, thread_deleted: typing.Callable[[], T_Result]) -> T_Result:
        if self is DeleteThreadResponseObject.THREAD_DELETED:
            return thread_deleted()
