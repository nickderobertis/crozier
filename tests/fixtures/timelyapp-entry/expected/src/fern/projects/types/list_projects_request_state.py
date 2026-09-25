

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListProjectsRequestState(enum.StrEnum):
    ALL = "all"
    ACTIVE = "active"
    ARCHIVED = "archived"

    def visit(
        self,
        all_: typing.Callable[[], T_Result],
        active: typing.Callable[[], T_Result],
        archived: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ListProjectsRequestState.ALL:
            return all_()
        if self is ListProjectsRequestState.ACTIVE:
            return active()
        if self is ListProjectsRequestState.ARCHIVED:
            return archived()
