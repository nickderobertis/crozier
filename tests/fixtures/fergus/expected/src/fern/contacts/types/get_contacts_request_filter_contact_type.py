

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetContactsRequestFilterContactType(enum.StrEnum):
    CUSTOMER = "CUSTOMER"
    SITE = "SITE"

    def visit(self, customer: typing.Callable[[], T_Result], site: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetContactsRequestFilterContactType.CUSTOMER:
            return customer()
        if self is GetContactsRequestFilterContactType.SITE:
            return site()
