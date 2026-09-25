

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class V1ProjectsCreateProjectBudgetType(enum.StrEnum):
    """
    Budget type: hours or money
    """

    H = "H"
    M = "M"

    def visit(self, h: typing.Callable[[], T_Result], m: typing.Callable[[], T_Result]) -> T_Result:
        if self is V1ProjectsCreateProjectBudgetType.H:
            return h()
        if self is V1ProjectsCreateProjectBudgetType.M:
            return m()
