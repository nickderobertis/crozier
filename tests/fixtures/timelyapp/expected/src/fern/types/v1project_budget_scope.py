

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class V1ProjectBudgetScope(enum.StrEnum):
    TAG = "tag"
    PROJECT = "project"

    def visit(self, tag: typing.Callable[[], T_Result], project: typing.Callable[[], T_Result]) -> T_Result:
        if self is V1ProjectBudgetScope.TAG:
            return tag()
        if self is V1ProjectBudgetScope.PROJECT:
            return project()
