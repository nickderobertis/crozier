

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetUsersRequestOrderBy(enum.StrEnum):
    ID = "id"
    LAST_ACTIVITY = "last_activity"
    FIRST_NAME = "first_name"
    LAST_NAME = "last_name"
    INDUSTRY = "industry"

    def visit(
        self,
        id: typing.Callable[[], T_Result],
        last_activity: typing.Callable[[], T_Result],
        first_name: typing.Callable[[], T_Result],
        last_name: typing.Callable[[], T_Result],
        industry: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetUsersRequestOrderBy.ID:
            return id()
        if self is GetUsersRequestOrderBy.LAST_ACTIVITY:
            return last_activity()
        if self is GetUsersRequestOrderBy.FIRST_NAME:
            return first_name()
        if self is GetUsersRequestOrderBy.LAST_NAME:
            return last_name()
        if self is GetUsersRequestOrderBy.INDUSTRY:
            return industry()
