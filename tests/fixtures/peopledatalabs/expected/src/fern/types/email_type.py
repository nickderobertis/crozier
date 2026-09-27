

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EmailType(enum.StrEnum):
    """
    The type of email either current_professional, professional, personal or null
    """

    PROFESSIONAL = "professional"
    PERSONAL = "personal"

    def visit(self, professional: typing.Callable[[], T_Result], personal: typing.Callable[[], T_Result]) -> T_Result:
        if self is EmailType.PROFESSIONAL:
            return professional()
        if self is EmailType.PERSONAL:
            return personal()
