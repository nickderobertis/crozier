

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BodyWithContentTypeContentTypeTemplateType(enum.StrEnum):
    VELOCITY = "VELOCITY"
    MUSTACHE = "MUSTACHE"

    def visit(self, velocity: typing.Callable[[], T_Result], mustache: typing.Callable[[], T_Result]) -> T_Result:
        if self is BodyWithContentTypeContentTypeTemplateType.VELOCITY:
            return velocity()
        if self is BodyWithContentTypeContentTypeTemplateType.MUSTACHE:
            return mustache()
