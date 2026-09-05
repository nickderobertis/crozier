

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProjectTemplateType(enum.StrEnum):
    TEMPLATE = "TEMPLATE"
    TUTORIAL = "TUTORIAL"
    HYPERTOOL = "HYPERTOOL"

    def visit(
        self,
        template: typing.Callable[[], T_Result],
        tutorial: typing.Callable[[], T_Result],
        hypertool: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ProjectTemplateType.TEMPLATE:
            return template()
        if self is ProjectTemplateType.TUTORIAL:
            return tutorial()
        if self is ProjectTemplateType.HYPERTOOL:
            return hypertool()
