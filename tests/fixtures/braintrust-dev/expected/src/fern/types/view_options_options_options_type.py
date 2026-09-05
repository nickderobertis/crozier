

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ViewOptionsOptionsOptionsType(enum.StrEnum):
    PROJECT = "project"
    EXPERIMENT = "experiment"

    def visit(self, project: typing.Callable[[], T_Result], experiment: typing.Callable[[], T_Result]) -> T_Result:
        if self is ViewOptionsOptionsOptionsType.PROJECT:
            return project()
        if self is ViewOptionsOptionsOptionsType.EXPERIMENT:
            return experiment()
