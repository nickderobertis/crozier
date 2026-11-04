

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ConfigCompatibilityLevel(enum.StrEnum):
    """
    Compatibility Level
    """

    BACKWARD = "BACKWARD"
    BACKWARD_TRANSITIVE = "BACKWARD_TRANSITIVE"
    FORWARD = "FORWARD"
    FORWARD_TRANSITIVE = "FORWARD_TRANSITIVE"
    FULL = "FULL"
    FULL_TRANSITIVE = "FULL_TRANSITIVE"
    NONE = "NONE"

    def visit(
        self,
        backward: typing.Callable[[], T_Result],
        backward_transitive: typing.Callable[[], T_Result],
        forward: typing.Callable[[], T_Result],
        forward_transitive: typing.Callable[[], T_Result],
        full: typing.Callable[[], T_Result],
        full_transitive: typing.Callable[[], T_Result],
        none: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ConfigCompatibilityLevel.BACKWARD:
            return backward()
        if self is ConfigCompatibilityLevel.BACKWARD_TRANSITIVE:
            return backward_transitive()
        if self is ConfigCompatibilityLevel.FORWARD:
            return forward()
        if self is ConfigCompatibilityLevel.FORWARD_TRANSITIVE:
            return forward_transitive()
        if self is ConfigCompatibilityLevel.FULL:
            return full()
        if self is ConfigCompatibilityLevel.FULL_TRANSITIVE:
            return full_transitive()
        if self is ConfigCompatibilityLevel.NONE:
            return none()
