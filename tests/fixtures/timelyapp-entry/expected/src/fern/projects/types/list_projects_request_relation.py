

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListProjectsRequestRelation(enum.StrEnum):
    ALL = "all"
    ASSIGNED = "assigned"
    CREATED = "created"

    def visit(
        self,
        all_: typing.Callable[[], T_Result],
        assigned: typing.Callable[[], T_Result],
        created: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ListProjectsRequestRelation.ALL:
            return all_()
        if self is ListProjectsRequestRelation.ASSIGNED:
            return assigned()
        if self is ListProjectsRequestRelation.CREATED:
            return created()
