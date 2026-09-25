

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetCustomersRequestSortField(enum.StrEnum):
    NAME = "name"
    CREATED_AT = "createdAt"

    def visit(self, name: typing.Callable[[], T_Result], created_at: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetCustomersRequestSortField.NAME:
            return name()
        if self is GetCustomersRequestSortField.CREATED_AT:
            return created_at()
