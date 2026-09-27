

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class HttpTemplateTemplateType(enum.StrEnum):
    VELOCITY = "VELOCITY"
    JAVASCRIPT = "JAVASCRIPT"
    MUSTACHE = "MUSTACHE"

    def visit(
        self,
        velocity: typing.Callable[[], T_Result],
        javascript: typing.Callable[[], T_Result],
        mustache: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is HttpTemplateTemplateType.VELOCITY:
            return velocity()
        if self is HttpTemplateTemplateType.JAVASCRIPT:
            return javascript()
        if self is HttpTemplateTemplateType.MUSTACHE:
            return mustache()
