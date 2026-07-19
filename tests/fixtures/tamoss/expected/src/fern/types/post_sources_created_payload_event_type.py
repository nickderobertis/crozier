

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostSourcesCreatedPayloadEventType(enum.StrEnum):
    SOURCES_CREATED = "sources/created"

    def visit(self, sources_created: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostSourcesCreatedPayloadEventType.SOURCES_CREATED:
            return sources_created()
