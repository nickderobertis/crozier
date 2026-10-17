

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class V1ListAllSnippetsRequestSortBy(enum.StrEnum):
    NAME = "name"
    INSERTED_AT = "inserted_at"

    def visit(self, name: typing.Callable[[], T_Result], inserted_at: typing.Callable[[], T_Result]) -> T_Result:
        if self is V1ListAllSnippetsRequestSortBy.NAME:
            return name()
        if self is V1ListAllSnippetsRequestSortBy.INSERTED_AT:
            return inserted_at()
