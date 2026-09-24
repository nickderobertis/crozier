

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateContactPayloadContactType(enum.StrEnum):
    CUSTOMER = "CUSTOMER"
    SITE = "SITE"

    def visit(self, customer: typing.Callable[[], T_Result], site: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateContactPayloadContactType.CUSTOMER:
            return customer()
        if self is CreateContactPayloadContactType.SITE:
            return site()
