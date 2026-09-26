

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListProjectsRequestFilter(enum.StrEnum):
    MINE = "mine"
    ACTIVE = "active"
    ALL = "all"
    ARCHIVED = "archived"

    def visit(
        self,
        mine: typing.Callable[[], T_Result],
        active: typing.Callable[[], T_Result],
        all_: typing.Callable[[], T_Result],
        archived: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ListProjectsRequestFilter.MINE:
            return mine()
        if self is ListProjectsRequestFilter.ACTIVE:
            return active()
        if self is ListProjectsRequestFilter.ALL:
            return all_()
        if self is ListProjectsRequestFilter.ARCHIVED:
            return archived()
