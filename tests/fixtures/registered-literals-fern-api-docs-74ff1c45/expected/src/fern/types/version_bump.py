

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class VersionBump(enum.StrEnum):
    MAJOR = "MAJOR"
    MINOR = "MINOR"
    PATCH = "PATCH"
    NO_CHANGE = "NO_CHANGE"

    def visit(
        self,
        major: typing.Callable[[], T_Result],
        minor: typing.Callable[[], T_Result],
        patch: typing.Callable[[], T_Result],
        no_change: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is VersionBump.MAJOR:
            return major()
        if self is VersionBump.MINOR:
            return minor()
        if self is VersionBump.PATCH:
            return patch()
        if self is VersionBump.NO_CHANGE:
            return no_change()
