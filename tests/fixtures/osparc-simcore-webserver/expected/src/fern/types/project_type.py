

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProjectType(enum.StrEnum):
    TEMPLATE = "TEMPLATE"
    STANDARD = "STANDARD"

    def visit(self, template: typing.Callable[[], T_Result], standard: typing.Callable[[], T_Result]) -> T_Result:
        if self is ProjectType.TEMPLATE:
            return template()
        if self is ProjectType.STANDARD:
            return standard()
