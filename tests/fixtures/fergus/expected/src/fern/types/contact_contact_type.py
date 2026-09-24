

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ContactContactType(enum.StrEnum):
    CUSTOMER = "CUSTOMER"
    SITE = "SITE"

    def visit(self, customer: typing.Callable[[], T_Result], site: typing.Callable[[], T_Result]) -> T_Result:
        if self is ContactContactType.CUSTOMER:
            return customer()
        if self is ContactContactType.SITE:
            return site()
