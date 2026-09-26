

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SchemeSummarySource(enum.StrEnum):
    BUILT_IN = "built_in"
    CUSTOM = "custom"

    def visit(self, built_in: typing.Callable[[], T_Result], custom: typing.Callable[[], T_Result]) -> T_Result:
        if self is SchemeSummarySource.BUILT_IN:
            return built_in()
        if self is SchemeSummarySource.CUSTOM:
            return custom()
