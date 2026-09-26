

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TemplateSummarySource(enum.StrEnum):
    BUILT_IN = "built_in"
    CUSTOM = "custom"

    def visit(self, built_in: typing.Callable[[], T_Result], custom: typing.Callable[[], T_Result]) -> T_Result:
        if self is TemplateSummarySource.BUILT_IN:
            return built_in()
        if self is TemplateSummarySource.CUSTOM:
            return custom()
