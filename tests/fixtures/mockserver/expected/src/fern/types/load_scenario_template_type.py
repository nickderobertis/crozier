

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LoadScenarioTemplateType(enum.StrEnum):
    """
    template engine used to render the per-iteration request path and body; only VELOCITY and MUSTACHE are supported for load steps (JAVASCRIPT is rejected)
    """

    VELOCITY = "VELOCITY"
    MUSTACHE = "MUSTACHE"

    def visit(self, velocity: typing.Callable[[], T_Result], mustache: typing.Callable[[], T_Result]) -> T_Result:
        if self is LoadScenarioTemplateType.VELOCITY:
            return velocity()
        if self is LoadScenarioTemplateType.MUSTACHE:
            return mustache()
