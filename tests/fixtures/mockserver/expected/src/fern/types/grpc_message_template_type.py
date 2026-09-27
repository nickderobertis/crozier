

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GrpcMessageTemplateType(enum.StrEnum):
    VELOCITY = "VELOCITY"
    JAVASCRIPT = "JAVASCRIPT"
    MUSTACHE = "MUSTACHE"

    def visit(
        self,
        velocity: typing.Callable[[], T_Result],
        javascript: typing.Callable[[], T_Result],
        mustache: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GrpcMessageTemplateType.VELOCITY:
            return velocity()
        if self is GrpcMessageTemplateType.JAVASCRIPT:
            return javascript()
        if self is GrpcMessageTemplateType.MUSTACHE:
            return mustache()
