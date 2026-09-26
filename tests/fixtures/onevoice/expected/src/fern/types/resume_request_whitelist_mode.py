

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ResumeRequestWhitelistMode(enum.StrEnum):
    INHERIT = "inherit"
    ALL = "all"
    EXPLICIT = "explicit"
    NONE = "none"
    EMPTY = ""

    def visit(
        self,
        inherit: typing.Callable[[], T_Result],
        all_: typing.Callable[[], T_Result],
        explicit: typing.Callable[[], T_Result],
        none: typing.Callable[[], T_Result],
        empty: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ResumeRequestWhitelistMode.INHERIT:
            return inherit()
        if self is ResumeRequestWhitelistMode.ALL:
            return all_()
        if self is ResumeRequestWhitelistMode.EXPLICIT:
            return explicit()
        if self is ResumeRequestWhitelistMode.NONE:
            return none()
        if self is ResumeRequestWhitelistMode.EMPTY:
            return empty()
