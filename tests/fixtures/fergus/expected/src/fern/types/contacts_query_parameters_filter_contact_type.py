

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ContactsQueryParametersFilterContactType(enum.StrEnum):
    CUSTOMER = "CUSTOMER"
    SITE = "SITE"

    def visit(self, customer: typing.Callable[[], T_Result], site: typing.Callable[[], T_Result]) -> T_Result:
        if self is ContactsQueryParametersFilterContactType.CUSTOMER:
            return customer()
        if self is ContactsQueryParametersFilterContactType.SITE:
            return site()
