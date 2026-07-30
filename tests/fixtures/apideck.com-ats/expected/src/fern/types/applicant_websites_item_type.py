

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ApplicantWebsitesItemType(enum.StrEnum):
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
        if self is ApplicantWebsitesItemType.PRIMARY:
            return primary()
        if self is ApplicantWebsitesItemType.SECONDARY:
            return secondary()
        if self is ApplicantWebsitesItemType.WORK:
            return work()
        if self is ApplicantWebsitesItemType.PERSONAL:
            return personal()
        if self is ApplicantWebsitesItemType.OTHER:
            return other()
