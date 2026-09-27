

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProjectWhitelistMode(enum.StrEnum):
    INHERIT = "inherit"
    ALL = "all"
    EXPLICIT = "explicit"
    NONE = "none"

    def visit(
        self,
        inherit: typing.Callable[[], T_Result],
        all_: typing.Callable[[], T_Result],
        explicit: typing.Callable[[], T_Result],
        none: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ProjectWhitelistMode.INHERIT:
            return inherit()
        if self is ProjectWhitelistMode.ALL:
            return all_()
        if self is ProjectWhitelistMode.EXPLICIT:
            return explicit()
        if self is ProjectWhitelistMode.NONE:
            return none()
