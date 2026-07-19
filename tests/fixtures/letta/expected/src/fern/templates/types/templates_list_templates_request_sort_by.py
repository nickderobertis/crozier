

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class TemplatesListTemplatesRequestSortBy(enum.StrEnum):
    UPDATED_AT = "updated_at"
    CREATED_AT = "created_at"

    def visit(self, updated_at: typing.Callable[[], T_Result], created_at: typing.Callable[[], T_Result]) -> T_Result:
        if self is TemplatesListTemplatesRequestSortBy.UPDATED_AT:
            return updated_at()
        if self is TemplatesListTemplatesRequestSortBy.CREATED_AT:
            return created_at()
