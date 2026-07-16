

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetActivateTypeRequestVersionBump(enum.StrEnum):
    MAJOR = "MAJOR"
    MINOR = "MINOR"

    def visit(self, major: typing.Callable[[], T_Result], minor: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetActivateTypeRequestVersionBump.MAJOR:
            return major()
        if self is GetActivateTypeRequestVersionBump.MINOR:
            return minor()
