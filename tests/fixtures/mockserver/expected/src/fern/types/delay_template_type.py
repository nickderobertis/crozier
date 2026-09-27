

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DelayTemplateType(enum.StrEnum):
    """
    template engine used to evaluate the delay template; only VELOCITY and MUSTACHE are supported
    """

    VELOCITY = "VELOCITY"
    MUSTACHE = "MUSTACHE"

    def visit(self, velocity: typing.Callable[[], T_Result], mustache: typing.Callable[[], T_Result]) -> T_Result:
        if self is DelayTemplateType.VELOCITY:
            return velocity()
        if self is DelayTemplateType.MUSTACHE:
            return mustache()
