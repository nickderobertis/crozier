

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProjectRequestWhitelistMode(enum.StrEnum):
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
        if self is ProjectRequestWhitelistMode.INHERIT:
            return inherit()
        if self is ProjectRequestWhitelistMode.ALL:
            return all_()
        if self is ProjectRequestWhitelistMode.EXPLICIT:
            return explicit()
        if self is ProjectRequestWhitelistMode.NONE:
            return none()
