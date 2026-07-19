

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostSourcesDeletedPayloadEventType(enum.StrEnum):
    SOURCES_DELETED = "sources/deleted"

    def visit(self, sources_deleted: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostSourcesDeletedPayloadEventType.SOURCES_DELETED:
            return sources_deleted()
