

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class VersionBump(str, enum.Enum):
    MAJOR = "MAJOR"
    MINOR = "MINOR"

    def visit(self, major: typing.Callable[[], T_Result], minor: typing.Callable[[], T_Result]) -> T_Result:
        if self is VersionBump.MAJOR:
            return major()
        if self is VersionBump.MINOR:
            return minor()
