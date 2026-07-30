

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EmailType(enum.StrEnum):
    PRIMARY = "primary"
    SECONDARY = "secondary"
    WORK = "work"
    PERSONAL = "personal"
    BILLING = "billing"
    OTHER = "other"

    def visit(
        self,
        primary: typing.Callable[[], T_Result],
        secondary: typing.Callable[[], T_Result],
        work: typing.Callable[[], T_Result],
        personal: typing.Callable[[], T_Result],
        billing: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EmailType.PRIMARY:
            return primary()
        if self is EmailType.SECONDARY:
            return secondary()
        if self is EmailType.WORK:
            return work()
        if self is EmailType.PERSONAL:
            return personal()
        if self is EmailType.BILLING:
            return billing()
        if self is EmailType.OTHER:
            return other()
