

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WebsiteType(enum.StrEnum):
    PRIMARY = "primary"
    SECONDARY = "secondary"
    WORK = "work"
    PERSONAL = "personal"
    OTHER = "other"

    def visit(
        self,
        primary: typing.Callable[[], T_Result],
        secondary: typing.Callable[[], T_Result],
        work: typing.Callable[[], T_Result],
        personal: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WebsiteType.PRIMARY:
            return primary()
        if self is WebsiteType.SECONDARY:
            return secondary()
        if self is WebsiteType.WORK:
            return work()
        if self is WebsiteType.PERSONAL:
            return personal()
        if self is WebsiteType.OTHER:
            return other()
