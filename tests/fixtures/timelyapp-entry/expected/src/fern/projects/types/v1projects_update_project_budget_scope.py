

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class V1ProjectsUpdateProjectBudgetScope(enum.StrEnum):
    """
    Budget scope: project-wide or per tag
    """

    TAG = "tag"
    PROJECT = "project"

    def visit(self, tag: typing.Callable[[], T_Result], project: typing.Callable[[], T_Result]) -> T_Result:
        if self is V1ProjectsUpdateProjectBudgetScope.TAG:
            return tag()
        if self is V1ProjectsUpdateProjectBudgetScope.PROJECT:
            return project()
