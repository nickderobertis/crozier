

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostSourcesUpdatedPayloadEventType(enum.StrEnum):
    SOURCES_UPDATED = "sources/updated"

    def visit(self, sources_updated: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostSourcesUpdatedPayloadEventType.SOURCES_UPDATED:
            return sources_updated()
