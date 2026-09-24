

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CollisionDetailsSeverity(enum.StrEnum):
    """
    Minimal stands for no emergency system activated during the collision. Minor only pretensioner system activated. Major for airbag and prentensioner activation.
    """

    MINIMAL = "Minimal"
    MINOR = "Minor"
    MAJOR = "Major"

    def visit(
        self,
        minimal: typing.Callable[[], T_Result],
        minor: typing.Callable[[], T_Result],
        major: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CollisionDetailsSeverity.MINIMAL:
            return minimal()
        if self is CollisionDetailsSeverity.MINOR:
            return minor()
        if self is CollisionDetailsSeverity.MAJOR:
            return major()
