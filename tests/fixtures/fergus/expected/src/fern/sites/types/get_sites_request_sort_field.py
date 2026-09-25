

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetSitesRequestSortField(enum.StrEnum):
    NAME = "name"
    CREATED_AT = "createdAt"

    def visit(self, name: typing.Callable[[], T_Result], created_at: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetSitesRequestSortField.NAME:
            return name()
        if self is GetSitesRequestSortField.CREATED_AT:
            return created_at()
