

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EmailType(enum.StrEnum):
    """
    The type of email account as described by the financial institution.
    """

    PRIMARY = "primary"
    SECONDARY = "secondary"
    OTHER = "other"

    def visit(
        self,
        primary: typing.Callable[[], T_Result],
        secondary: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EmailType.PRIMARY:
            return primary()
        if self is EmailType.SECONDARY:
            return secondary()
        if self is EmailType.OTHER:
            return other()
