

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetContactsRequestSortField(enum.StrEnum):
    FIRST_NAME = "firstName"
    LAST_NAME = "lastName"
    CREATED_AT = "createdAt"

    def visit(
        self,
        first_name: typing.Callable[[], T_Result],
        last_name: typing.Callable[[], T_Result],
        created_at: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetContactsRequestSortField.FIRST_NAME:
            return first_name()
        if self is GetContactsRequestSortField.LAST_NAME:
            return last_name()
        if self is GetContactsRequestSortField.CREATED_AT:
            return created_at()
