

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetActivateTypeRequestVersionBump(str, enum.Enum):
    MAJOR = "MAJOR"
    MINOR = "MINOR"

    def visit(self, major: typing.Callable[[], T_Result], minor: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetActivateTypeRequestVersionBump.MAJOR:
            return major()
        if self is GetActivateTypeRequestVersionBump.MINOR:
            return minor()
