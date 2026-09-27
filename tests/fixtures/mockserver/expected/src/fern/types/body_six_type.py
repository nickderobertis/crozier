

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BodySixType(enum.StrEnum):
    REGEX = "REGEX"

    def visit(self, regex: typing.Callable[[], T_Result]) -> T_Result:
        if self is BodySixType.REGEX:
            return regex()
