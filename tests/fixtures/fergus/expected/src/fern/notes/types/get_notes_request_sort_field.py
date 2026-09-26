

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetNotesRequestSortField(enum.StrEnum):
    CREATED_AT = "created_at"

    def visit(self, created_at: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetNotesRequestSortField.CREATED_AT:
            return created_at()
